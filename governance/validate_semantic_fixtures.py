#!/usr/bin/env python3
"""Validate P0-10 fixture semantics and P0-06 claimant-assertion negatives."""
from pathlib import Path
import copy, hashlib, json, re, sys
from jsonschema import Draft202012Validator, RefResolver
ROOT=Path(__file__).resolve().parents[1]

def loadj(rel): return json.loads((ROOT/rel).read_text())
def sha(rel): return hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
def get_path(obj,path):
    cur=obj
    for token in re.findall(r'[^.\[\]]+|\d+(?=\])',path):
        cur=cur[int(token)] if token.isdigit() else cur[token]
    return cur
def set_path(obj,path,value):
    tokens=re.findall(r'[^.\[\]]+|\d+(?=\])',path); cur=obj
    for token in tokens[:-1]: cur=cur[int(token)] if token.isdigit() else cur[token]
    last=tokens[-1]
    if last.isdigit(): cur[int(last)] = value
    else: cur[last] = value

def semantic_issues(obj, groups):
    out=[]
    for group,paths in groups.items():
        vals=[]
        try:
            vals=[get_path(obj,p) for p in paths]
        except Exception as e:
            out.append({'group':group,'error':str(e),'paths':paths}); continue
        if len({json.dumps(v,sort_keys=True) for v in vals})>1:
            out.append({'group':group,'paths':paths,'values':vals})
    return out
issues=[]; checks=[]
def check(name,ok,detail=None):
    checks.append({'check':name,'status':'PASS' if ok else 'FAIL','detail':detail})
    if not ok: issues.append(f'{name}: {detail}')

fm=loadj('conformance/fixture-mapping.json')
vec=loadj('conformance/semantic-fixtures/AGCP-Semantic-Fixture-Test-Vectors.json')
check('semantic_fixture_count',fm.get('semantic_fixture_count')==14,fm.get('semantic_fixture_count'))
check('semantic_vector_catalog',fm.get('semantic_vector_catalog')=='conformance/semantic-fixtures/AGCP-Semantic-Fixture-Test-Vectors.json')
check('claimant_vector_catalog',fm.get('claimant_assertion_vector_catalog')=='conformance/command-record/AGCP-Governance-Approval-Command-Record-Test-Vectors.json')

# Schema store and structural validation of all controlled fixtures.
store={}
for p in (ROOT/'schemas').glob('*.json'):
    try:
        s=json.loads(p.read_text()); store[s.get('$id',p.as_uri())]=s
    except Exception: pass
struct=[]
for f in fm['fixtures']:
    schema=loadj(f['schema_file']); obj=loadj(f['example_file'])
    resolver=RefResolver(base_uri=(ROOT/f['schema_file']).as_uri(),referrer=schema,store=store)
    errs=sorted(e.message for e in Draft202012Validator(schema,resolver=resolver).iter_errors(obj))
    struct.append({'fixture_id':f['fixture_id'],'file':f['example_file'],'valid':not errs,'errors':errs})
check('all_controlled_fixtures_schema_valid',all(x['valid'] for x in struct),[x for x in struct if not x['valid']])

# Positive semantic fixtures.
pos=[]
for f in vec['positive_fixtures']:
    obj=loadj(f['file']); sem=semantic_issues(obj,f['equivalence_groups'])
    legacy=[]
    def walk(x,path=''):
        if isinstance(x,dict):
            for k,v in x.items(): walk(v,f'{path}.{k}' if path else k)
        elif isinstance(x,list):
            for i,v in enumerate(x): walk(v,f'{path}[{i}]')
        elif x in {'tenant-id-1','governance-domain-id-1','proposal-id-1','policy-id-1','canonical-state-id-1'}:
            legacy.append({'path':path,'value':x})
    walk(obj)
    pos.append({'file':f['file'],'semantic_issues':sem,'legacy_placeholders':legacy})
check('fourteen_positive_fixtures_semantically_consistent',len(pos)==14 and all(not x['semantic_issues'] and not x['legacy_placeholders'] for x in pos),[x for x in pos if x['semantic_issues'] or x['legacy_placeholders']])

# Semantic negative vectors must be structurally valid but semantically inconsistent.
rule_by_file={x['file']:x['equivalence_groups'] for x in vec['positive_fixtures']}
neg=[]
for v in vec['semantic_mismatch_vectors']:
    base=loadj(v['base_fixture']); mut=copy.deepcopy(base); set_path(mut,v['mutation']['path'],v['mutation']['value'])
    sem=semantic_issues(mut,rule_by_file[v['base_fixture']])
    # Confirm the mutation does not merely fail JSON Schema; these vectors prove semantic checking beyond schema validity.
    fm_entry=next(x for x in fm['fixtures'] if x['example_file']==v['base_fixture'])
    schema=loadj(fm_entry['schema_file']); resolver=RefResolver(base_uri=(ROOT/fm_entry['schema_file']).as_uri(),referrer=schema,store=store)
    schema_errs=[e.message for e in Draft202012Validator(schema,resolver=resolver).iter_errors(mut)]
    neg.append({'id':v['id'],'mismatch_class':v['mismatch_class'],'schema_valid':not schema_errs,'semantic_issues':sem})
check('semantic_negative_vector_count',len(neg)==10,len(neg))
check('semantic_negatives_schema_valid_but_semantically_invalid',all(x['schema_valid'] and x['semantic_issues'] for x in neg),neg)

# Existing P0-06 claimant-assertion negatives remain explicit and rejected by DS-045.
cmd=loadj('conformance/command-record/AGCP-Governance-Approval-Command-Record-Test-Vectors.json')
submission=loadj('schemas/examples/ds045-governance-approval-submission-valid.json'); ss=loadj('schemas/governance_approval_submission.json')
resolver=RefResolver(base_uri=(ROOT/'schemas/governance_approval_submission.json').as_uri(),referrer=ss,store=store); sv=Draft202012Validator(ss,resolver=resolver)
claim=[]
for v in cmd['negative_vectors']:
    mut=copy.deepcopy(submission); m=v['mutation']; mut[m['add_top_level_field']]=m['value']; errs=[e.message for e in sv.iter_errors(mut)]
    claim.append({'id':v['id'],'rejected':bool(errs),'errors':errs})
check('claimant_assertion_negative_vector_count',len(claim)==15,len(claim))
check('all_claimant_assertion_vectors_rejected',all(x['rejected'] for x in claim),[x for x in claim if not x['rejected']])

report={'release_context':{'repository_release_target':'v2.0.4','repository_release_target_status':'PUBLIC_REVIEW_CONTROLLED_BASELINE','controlling_published_baseline':'v2.0.4','controlling_baseline_status':'PUBLIC_REVIEW_CONTROLLED_BASELINE','baseline_date':'2026-08-05','artifact_lifecycle_state':'CURRENT'},
 'report_id':'AGCP-P0-10-P0-06-SEMANTIC-FIXTURE-VALIDATION',
 'status':'PASS' if not issues else 'FAIL','validated_at':'2026-08-03','findings':['P0-10','P0-06'],
 'controlled_fixture_count':len(fm['fixtures']),'corrected_positive_fixture_count':len(pos),
 'semantic_negative_vector_count':len(neg),'claimant_assertion_negative_vector_count':len(claim),
 'source_hashes':{r:sha(r) for r in [
  'conformance/fixture-mapping.json','conformance/semantic-fixtures/AGCP-Semantic-Fixture-Test-Vectors.json',
  'conformance/command-record/AGCP-Governance-Approval-Command-Record-Test-Vectors.json',
  'schemas/governance_approval_submission.json','schemas/examples/ds045-governance-approval-submission-valid.json',
  'governance/validate_semantic_fixtures.py',] + [x['file'] for x in vec['positive_fixtures']]},
 'positive_fixture_validation':pos,'semantic_negative_validation':neg,'claimant_assertion_validation':claim,
 'checks':checks,'issues':issues
}
(ROOT/'governance/AGCP-semantic-fixture-validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'checks':len(checks),'issues':issues},indent=2))
sys.exit(0 if not issues else 1)
