#!/usr/bin/env python3
from pathlib import Path
import json, re, hashlib, copy, sys
import yaml
from jsonschema import Draft202012Validator, RefResolver

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'conformance' / 'AGCP-v2.1.x-aggregate-conformance-layer-validation.json'

def loadj(rel): return json.loads((ROOT/rel).read_text())
def loady(rel): return yaml.safe_load((ROOT/rel).read_text())
def sha(rel): return hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()

checks=[]; errors=[]; warnings=[]
def check(cid, ok, detail=None):
    checks.append({'check_id':cid,'status':'PASS' if ok else 'FAIL','detail':detail})
    if not ok: errors.append(f'{cid}: {detail}')

def warn(cid, detail): warnings.append(f'{cid}: {detail}')

def ns_list(text): return re.findall(r'NS-[0-9A-Za-z.]+(?:-[0-9A-Za-z.]+)?', text or '')

# --- Formal Test Cases ---
formal={}
for p in sorted((ROOT/'conformance/tests').glob('TC*.md')):
    txt=p.read_text()
    matches=list(re.finditer(r'^# (TC-\d{3}) — (.+)$',txt,re.M))
    for i,m in enumerate(matches):
        tc=m.group(1); title=m.group(2).strip(); section=txt[m.start(): matches[i+1].start() if i+1<len(matches) else len(txt)]
        def line(label):
            mm=re.search(r'^- '+re.escape(label)+r':\s*(.*)$',section,re.M)
            return mm.group(1).strip() if mm else ''
        cr_m=re.search(r'^- Primary Conformance Requirement: \*\*(CR-\d{3}) —',section,re.M)
        cr=cr_m.group(1) if cr_m else None
        direct=ns_list(line('Direct Test-Generating NS IDs'))
        cond=ns_list(line('Conditional NS IDs'))
        supp=ns_list(line('Supporting/Contextual NS IDs'))
        direct_heads=re.findall(r'^### '+re.escape(tc)+r'-A\d+ — (NS-[0-9A-Za-z.]+(?:-[0-9A-Za-z.]+)?)$',section,re.M)
        cond_heads=re.findall(r'^### '+re.escape(tc)+r'-C\d+ — (NS-[0-9A-Za-z.]+(?:-[0-9A-Za-z.]+)?)$',section,re.M)
        formal[tc]={'title':title,'cr_id':cr,'direct':direct,'conditional':cond,'supporting':supp,'file':p.name,
                    'direct_heads':direct_heads,'conditional_heads':cond_heads}

tc_expected=[f'TC-{i:03d}' for i in range(1,123)]
cr_expected=[f'CR-{i:03d}' for i in range(1,123)]
check('FORMAL_TC_COUNT',len(formal)==122,len(formal))
check('FORMAL_TC_CONTINUOUS',sorted(formal)==tc_expected,{'missing':sorted(set(tc_expected)-set(formal)),'extra':sorted(set(formal)-set(tc_expected))})
check('FORMAL_CR_ONE_TO_ONE',all(formal[t]['cr_id']==f'CR-{int(t[-3:]):03d}' for t in tc_expected),[(t,formal.get(t,{}).get('cr_id')) for t in tc_expected if formal.get(t,{}).get('cr_id')!=f'CR-{int(t[-3:]):03d}'])
check('FORMAL_DIRECT_ASSERTION_HEADINGS',all(set(v['direct'])==set(v['direct_heads']) for v in formal.values()),[t for t,v in formal.items() if set(v['direct'])!=set(v['direct_heads'])])
check('FORMAL_CONDITIONAL_ASSERTION_HEADINGS',all(set(v['conditional'])==set(v['conditional_heads']) for v in formal.values()),[t for t,v in formal.items() if set(v['conditional'])!=set(v['conditional_heads'])])

# --- Formal synchronization delta ---
sync=loadj('conformance/v2.1.x-formal-test-sync.json')
formal_change=set(sync['formal_traceability_or_assertion_tcs']); regression=set(sync['regression_scenario_only_tcs'])
check('FORMAL_SYNC_COUNTS',len(formal_change)==42 and len(regression)==22 and len(formal_change|regression)==64,{'formal':len(formal_change),'regression':len(regression),'total':len(formal_change|regression)})
new_ns=sync['new_ns_disposition']
new_ns_errors=[]
for ns,disp in new_ns.items():
    tc=disp['tc_id']; rel=disp['relationship'].lower(); f=formal.get(tc,{})
    bucket='supporting' if rel in {'support','supporting','contextual'} else ('conditional' if rel=='conditional' else 'direct')
    if ns not in f.get(bucket,[]): new_ns_errors.append((ns,tc,rel))
check('NEW_NS_DISPOSITIONS_36',len(new_ns)==36 and not new_ns_errors,{'count':len(new_ns),'mismatches':new_ns_errors})
retired={'NS-8.6A-01','NS-8.6A-03','NS-9.1-01'}
active_formal_ns={x for f in formal.values() for b in ('direct','conditional','supporting') for x in f[b]}
check('RETIRED_NS_NOT_ACTIVE',not (retired & active_formal_ns),sorted(retired & active_formal_ns))

# --- Test Matrix ---
mtxt=(ROOT/'conformance/AGCP-Test-Matrix.md').read_text()
rows={}
for line in mtxt.splitlines():
    m=re.match(r'^\| `(TC-\d{3})` \| `(CR-\d{3})` \| (.*?) \| (.*?) \| (.*?) \| (\d+) \| (\d+) \| (\d+) \| (.*?) \|$',line)
    if m:
        rows[m.group(1)]={'cr_id':m.group(2),'title':m.group(3).strip(),'direct':int(m.group(6)),'conditional':int(m.group(7)),'supporting':int(m.group(8)),'class':m.group(9).strip()}
check('MATRIX_TC_COUNT',len(rows)==122,len(rows))
mat_mismatch=[]
for tc in tc_expected:
    r=rows.get(tc); f=formal.get(tc)
    if not r or not f: continue
    if r['cr_id']!=f['cr_id'] or r['title']!=f['title'] or r['direct']!=len(f['direct']) or r['conditional']!=len(f['conditional']) or r['supporting']!=len(f['supporting']):
        mat_mismatch.append(tc)
check('MATRIX_MATCHES_FORMAL_TC',not mat_mismatch,mat_mismatch)

# --- Catalogs ---
schema_cat=loadj('schemas/catalog/schema-catalog.json'); ds_ids={e['ds_id'] for e in schema_cat['implemented_schemas']}
if_cat=loadj('api/interface-catalog.json'); if_ids={e['if_id'] for e in if_cat['interfaces']}
reg_cat=loadj('registries/registry-entry-catalog.json'); reg_ids={e['reg_id'] for e in reg_cat['entries']}

# --- Test Mapping ---
tm=loadj('conformance/test-mapping.json'); tests=tm['tests']; bytc={e['tc_id']:e for e in tests}
check('TEST_MAPPING_COUNT',len(tests)==122 and len(bytc)==122,{'records':len(tests),'unique':len(bytc)})
map_mismatch=[]; file_missing=[]; id_missing=[]
for tc in tc_expected:
    e=bytc.get(tc); f=formal.get(tc)
    if not e or not f: continue
    if e['cr_id']!=f['cr_id'] or e['title']!=f['title'] or e.get('direct_ns_ids',[])!=f['direct'] or e.get('conditional_ns_ids',[])!=f['conditional'] or e.get('contextual_ns_ids',[])!=f['supporting'] or e.get('file')!=f['file']:
        map_mismatch.append(tc)
    for rel in e.get('schema_files',[])+e.get('fixture_files',[])+e.get('profile_artifact_refs',[]):
        if not (ROOT/rel).is_file(): file_missing.append((tc,rel))
    for x in e.get('ds_ids',[]):
        if x not in ds_ids: id_missing.append((tc,'DS',x))
    for x in e.get('if_ids',[]):
        if x not in if_ids: id_missing.append((tc,'IF',x))
    for x in e.get('registry_ids',[]):
        if x not in reg_ids: id_missing.append((tc,'REG',x))
check('TEST_MAPPING_MATCHES_FORMAL_TC',not map_mismatch,map_mismatch)
check('TEST_MAPPING_REFERENCED_FILES_EXIST',not file_missing,file_missing[:50])
check('TEST_MAPPING_CATALOG_IDS_RESOLVE',not id_missing,id_missing[:50])
check('TEST_MAPPING_CHANGE_CLASS_COUNTS',sum(1 for e in tests if e.get('v2_1_x_change_class')=='FORMAL_ASSERTION_TRACEABILITY')==42 and sum(1 for e in tests if e.get('v2_1_x_change_class')=='REGRESSION_SCENARIO')==22,{
    'formal':sum(1 for e in tests if e.get('v2_1_x_change_class')=='FORMAL_ASSERTION_TRACEABILITY'),
    'regression':sum(1 for e in tests if e.get('v2_1_x_change_class')=='REGRESSION_SCENARIO')})

# --- Test-control mapping and standardized vocabularies ---
d050=loadj('schemas/test_control_request.json'); controls=set(d050['properties']['control_type']['enum'])
d046=loadj('schemas/governance_observation_event.json'); obs=set(d046['properties']['observation_type']['enum'])
tcm=loadj('conformance/test-control-mapping.json'); cent=tcm['entries']; cby={e['tc_id']:e for e in cent}
check('TEST_CONTROL_MAPPING_COUNT',len(cent)==122 and len(cby)==122,{'records':len(cent),'unique':len(cby)})
unknown_controls=[]; unknown_obs=[]; control_binding_mismatch=[]
for e in cent:
    for c in e.get('recommended_test_controls',[]):
        if c not in controls: unknown_controls.append((e['tc_id'],c))
    if e.get('cleanup_control') and e['cleanup_control'] not in controls: unknown_controls.append((e['tc_id'],e['cleanup_control']))
    for b in e.get('control_bindings',[]):
        c=b.get('control_type')
        if c not in controls: unknown_controls.append((e['tc_id'],c))
        if c not in e.get('recommended_test_controls',[]): control_binding_mismatch.append((e['tc_id'],c))
    for o in e.get('recommended_observation_points',[]):
        if o not in obs: unknown_obs.append((e['tc_id'],o))
check('TEST_CONTROL_VOCABULARY_RESOLVES',not unknown_controls,unknown_controls)
check('OBSERVATION_POINT_VOCABULARY_RESOLVES',not unknown_obs,unknown_obs)
check('CONTROL_BINDINGS_MATCH_RECOMMENDATIONS',not control_binding_mismatch,control_binding_mismatch)
check('CONTROL_MAPPING_COUNTS',sum(len(e.get('control_bindings',[])) for e in cent)>=108 and sum(len(e.get('recommended_observation_points',[])) for e in cent)==477,{
    'bindings':sum(len(e.get('control_bindings',[])) for e in cent),'observations':sum(len(e.get('recommended_observation_points',[])) for e in cent)})

# --- Harness checks and vectors ---
hc=loadj('conformance/harness-checks.json'); hchecks=hc['checks']; hids=[e['check_id'] for e in hchecks]; hidset=set(hids)
hs=loady('conformance/AGCP-Conformance-Harness-Spec.yml'); vectors=hs['tests']; vids=[e['id'] for e in vectors]; vidset=set(vids)
md_vids=set(re.findall(r'^## (TV-[A-Z0-9-]+) —', (ROOT/'conformance/AGCP-Conformance-Test-Vectors.md').read_text(), re.M))
check('HARNESS_CHECK_COUNT_UNIQUE',len(hids)==21 and len(hidset)==21 and hc.get('check_count')==21,{'records':len(hids),'unique':len(hidset),'declared':hc.get('check_count')})
check('HARNESS_VECTOR_COUNT_UNIQUE',len(vids)==135 and len(vidset)==135 and hs['meta']['vector_catalog']['expected_vector_count']==135,{'records':len(vids),'unique':len(vidset),'expected':hs['meta']['vector_catalog']['expected_vector_count']})
check('HARNESS_YAML_MARKDOWN_VECTOR_SET_EQUAL',vidset==md_vids,{'yaml_only':sorted(vidset-md_vids),'markdown_only':sorted(md_vids-vidset)})
unknown_harness_refs=[]; used_checks=set(); used_vectors=set()
for e in tests:
    for x in e.get('harness_check_ids',[]):
        used_checks.add(x)
        if x not in hidset: unknown_harness_refs.append((e['tc_id'],'check',x))
    for x in e.get('test_vector_ids',[])+e.get('supporting_test_vector_ids',[]):
        used_vectors.add(x)
        if x not in vidset: unknown_harness_refs.append((e['tc_id'],'vector',x))
for c in hchecks:
    for x in c.get('applies_to',{}).get('test_vectors',[]):
        if x not in vidset: unknown_harness_refs.append((c['check_id'],'vector',x))
    for rel in c.get('applies_to',{}).get('schemas',[])+c.get('applies_to',{}).get('fixtures',[]):
        if not (ROOT/rel).is_file(): file_missing.append((c['check_id'],rel))
check('HARNESS_REFERENCES_RESOLVE',not unknown_harness_refs,unknown_harness_refs)
check('ALL_HARNESS_CHECKS_MAPPED',used_checks==hidset,{'unmapped':sorted(hidset-used_checks)})
check('ALL_HARNESS_VECTORS_MAPPED',used_vectors==vidset,{'unmapped':sorted(vidset-used_vectors)})

required_new={f'TV-IAS-{i:03d}' for i in range(1,6)}|{f'TV-GRF-{i:03d}' for i in range(1,5)}|{f'TV-PEP-{i:03d}' for i in range(1,7)}|{f'TV-EXEC-{i:03d}' for i in range(1,3)}
check('V2_1_X_REQUIRED_NEW_VECTORS_PRESENT',required_new <= vidset,sorted(required_new-vidset))

# Every internal injection need must be standardized by DS-050 and represented by a vector.
need_tcs={e['tc_id']:e for e in cent if e.get('additional_harness_injection_needs')}
unresolved=[]
for tc,e in need_tcs.items():
    for n in e.get('additional_harness_injection_needs',[]):
        support=n.get('standardized_if005_support',[])
        if not support or any(c not in controls for c in support): unresolved.append((tc,n.get('need'),support))
vector_controls={}
for v in vectors:
    vector_controls[v['id']]={x.get('control_type') for x in v.get('arrange',{}).get('test_controls',[]) if isinstance(x,dict)}
representation_ok=(
    'TARGET_EXECUTION_FIXTURE' in (vector_controls.get('TV-EXEC-001',set())|vector_controls.get('TV-EXEC-002',set())) and
    'ENFORCEMENT_PATH_FAULT_FIXTURE' in vector_controls.get('TV-PEP-003',set()) and
    'ENFORCEMENT_PATH_FAULT_FIXTURE' in vector_controls.get('TV-PEP-004',set()) and
    'ENFORCEMENT_PATH_FAULT_FIXTURE' in vector_controls.get('TV-PEP-005',set()) and
    'ENFORCEMENT_PATH_FAULT_FIXTURE' in vector_controls.get('TV-PEP-006',set())
)
check('NO_UNRESOLVED_INTERNAL_INJECTION_NEEDS',not unresolved and representation_ok,{'unresolved':unresolved,'vector_representation':representation_ok})
check('ALL_TCS_HAVE_DIRECT_VECTOR',all(e.get('test_vector_ids') for e in tests),[e['tc_id'] for e in tests if not e.get('test_vector_ids')])

# --- Controlled fixture structural validation ---
fm=loadj('conformance/fixture-mapping.json')
store={}
for p in (ROOT/'schemas').glob('*.json'):
    try:
        s=json.loads(p.read_text()); store[s.get('$id',p.as_uri())]=s
    except Exception: pass
fixture_errors=[]
for f in fm['fixtures']:
    try:
        schema=loadj(f['schema_file']); obj=loadj(f['example_file'])
        resolver=RefResolver(base_uri=(ROOT/f['schema_file']).as_uri(),referrer=schema,store=store)
        errs=sorted(e.message for e in Draft202012Validator(schema,resolver=resolver).iter_errors(obj))
        if errs: fixture_errors.append((f['fixture_id'],errs[:5]))
    except Exception as ex: fixture_errors.append((f.get('fixture_id'),[str(ex)]))
check('CONTROLLED_FIXTURE_COUNT_AND_SCHEMA_VALIDITY',len(fm['fixtures'])==36 and not fixture_errors,{'count':len(fm['fixtures']),'errors':fixture_errors})
sem_report=loadj('governance/AGCP-semantic-fixture-validation.json')
check('SEMANTIC_FIXTURE_VALIDATION_PASS',sem_report.get('status')=='PASS' and not sem_report.get('issues'),{'status':sem_report.get('status'),'issues':sem_report.get('issues')})

# --- Architecture-critical request/realization separation ---
ds018=loadj('schemas/commit_boundary_request.json'); ex018=loadj('schemas/examples/ds018-commit-boundary-request-single.json')
props=set(ds018.get('properties',{})); forbidden={'enforcement_context','authority_rederivation_result_ref','qualified_evidence_refs','resulting_state_validation_result_ref','state_qualification_result_ref','pep_profile_ref'}
check('DS018_DOES_NOT_ACCEPT_GRF_DERIVED_AUTHORITY_CONTEXT',not(props & forbidden) and not(set(ex018)&forbidden),{'schema_forbidden':sorted(props&forbidden),'example_forbidden':sorted(set(ex018)&forbidden)})
commit_vector_forbidden=[]
for v in vectors:
    req=v.get('request',{})
    if req.get('path')=='/agcp/v2/commit-boundary/commit' and isinstance(req.get('body'),dict):
        bad=set(req['body']) & forbidden
        if bad: commit_vector_forbidden.append((v['id'],sorted(bad)))
check('COMMIT_VECTORS_DO_NOT_INJECT_DERIVED_ENFORCEMENT_CONTEXT',not commit_vector_forbidden,commit_vector_forbidden)

# --- Prior controlled step reports ---
prior_reports=[
 'conformance/AGCP-v2.1.x-formal-test-sync-validation.json',
 'conformance/AGCP-v2.1.x-test-matrix-validation.json',
 'conformance/AGCP-v2.1.x-test-mapping-validation.json',
 'conformance/AGCP-v2.1.x-test-control-mapping-validation.json',
 'conformance/AGCP-v2.1.x-harness-vector-check-validation.json']
prior_status={p:loadj(p).get('status') for p in prior_reports}
check('PRIOR_CONTROLLED_STEP_REPORTS_PASS',all(v=='PASS' for v in prior_status.values()),prior_status)

# Source hashes for aggregate-controlled conformance inputs (RTM intentionally excluded until next step).
source_files=[
 'conformance/AGCP-Test-Matrix.md','conformance/test-mapping.json','conformance/test-control-mapping.json',
 'conformance/harness-checks.json','conformance/AGCP-Conformance-Harness-Spec.yml','conformance/AGCP-Conformance-Test-Vectors.md',
 'conformance/fixture-mapping.json','conformance/semantic-fixtures/AGCP-Semantic-Fixture-Test-Vectors.json',
 'schemas/test_control_request.json','schemas/test_control_result.json','schemas/governance_observation_event.json','schemas/management_capabilities_response.json','schemas/governance_actuation_request.json','schemas/governance_actuation_result.json','conformance/AGCP-Management-Plane-Harness-Spec.yml','schemas/commit_boundary_request.json']
source_hashes={p:sha(p) for p in source_files}

report={
 'validation_id':'AGCP-v2.1.x-AGGREGATE-CONFORMANCE-LAYER-VALIDATION-2026-10-03',
 'status':'PASS' if not errors else 'FAIL',
 'validated_at':'2026-10-03',
 'scope':'Pre-RTM aggregate validation of the synchronized Formal TC, Test Matrix, test mapping, test-control mapping, Harness Check, Harness Test Vector, fixture, DS-050, and DS-046 conformance layers.',
 'formal_test_case_count':len(formal),
 'test_mapping_count':len(tests),
 'test_control_mapping_count':len(cent),
 'harness_check_count':len(hchecks),
 'harness_test_vector_count':len(vectors),
 'controlled_fixture_count':len(fm['fixtures']),
 'new_ns_disposition_count':len(new_ns),
 'formal_change_count':len(formal_change),
 'regression_change_count':len(regression),
 'test_control_binding_count':sum(len(e.get('control_bindings',[])) for e in cent),
 'observation_reference_count':sum(len(e.get('recommended_observation_points',[])) for e in cent),
 'additional_harness_injection_need_count':sum(len(e.get('additional_harness_injection_needs',[])) for e in cent),
 'retired_ns_active_reference_count':len(retired & active_formal_ns),
 'semantic_fixture_correction_applied':True,
 'semantic_fixture_correction_summary':'Removed obsolete DS-018 assumptions that the caller supplies GRF-derived authority/evidence/DS-029 content; remapped negative semantic vectors to the current DS-018/DS-019/DS-026/DS-029/DS-039 boundaries.',
 'rtm_status':'PENDING_FINAL_RTM_SYNCHRONIZATION',
 'next_controlled_step':'FINAL_RTM_SYNCHRONIZATION',
 'limitations':[
   'This validation does not regenerate or approve the RTM; the RTM is the next controlled step.',
   'This validation does not establish implementation conformance; it validates repository conformance-layer internal consistency.',
   'TC-073, TC-075, and TC-090 retain genuine external-dependency requirements that cannot be replaced by IF-005 simulation.',
   'Repository-release manifest/hash synchronization is a later release-validation activity and is not used as a pass criterion for this pre-RTM conformance-layer validation.'
 ],
 'source_hashes':source_hashes,
 'checks':checks,
 'warnings':warnings,
 'errors':errors
}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'checks_passed':sum(c['status']=='PASS' for c in checks),'checks_total':len(checks),'errors':errors,'warnings':warnings},indent=2))
sys.exit(0 if not errors else 1)
