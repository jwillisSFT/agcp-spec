#!/usr/bin/env python3
"""Validate P2-01 release, publication, lifecycle, version, and baseline metadata."""
from __future__ import annotations
from pathlib import Path
import csv, copy, hashlib, json, re, sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = 'governance/release-lifecycle-metadata.json'
issues=[]; checks=[]

def loadj(rel): return json.loads((ROOT/rel).read_text())
def sha(rel): return hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
def check(name, ok, detail=None):
    checks.append({'check':name,'status':'PASS' if ok else 'FAIL','detail':detail})
    if not ok: issues.append(f'{name}: {detail}')

def canon(o): return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def dig(o): return hashlib.sha256(canon(o)).hexdigest()

p=loadj(POLICY_PATH)
ctx=p['validation_report_release_context']
check('policy_values', p['repository_release_target']=='v2.0.1' and p['repository_release_target_status']=='UNRELEASED_ACCUMULATED_CORRECTION_SET' and p['controlling_published_baseline']['release_status']=='PUBLIC_REVIEW_CONTROLLED_BASELINE' and p['controlling_published_baseline']['baseline_date']=='2026-07-30' and p['current_artifact_lifecycle_state']=='CURRENT')

catalogs={
 'schema':('schemas/catalog/schema-catalog.json','1.0.50'),
 'interface':('api/interface-catalog.json','1.0.5'),
 'registry':('registries/registry-entry-catalog.json','1.0.3'),
}
for name,(rel,ver) in catalogs.items():
    d=loadj(rel)
    check(f'{name}_catalog_version', d['catalog_version']==ver, d.get('catalog_version'))
    check(f'{name}_catalog_metadata', d.get('specification_version')=='v2.0.1' and d.get('publication_status')=='CURRENT' and d.get('artifact_lifecycle_state')=='CURRENT' and d.get('repository_release_target')=='v2.0.1' and d.get('repository_release_target_status')=='UNRELEASED_ACCUMULATED_CORRECTION_SET' and d.get('release_status')=='PUBLIC_REVIEW_CONTROLLED_BASELINE' and d.get('controlling_published_baseline')=='v2.0.0' and d.get('baseline_date')=='2026-07-30', {k:d.get(k) for k in ['specification_version','publication_status','artifact_lifecycle_state','repository_release_target','repository_release_target_status','release_status','controlling_published_baseline','baseline_date']})

sc=loadj('schemas/catalog/schema-catalog.json')
check('schema_catalog_summary', sc['summary']['implemented_schema_count']==44 and sc['summary']['rtm_rows_with_ds_assignments']==122 and sc['summary']['rtm_rows_with_if_assignments']==84 and sc['summary']['registry_entry_count']==94, sc['summary'])
check('schema_entry_spec_versions', all(e['specification_version']=='v2.0.1' for e in sc['implemented_schemas']+sc.get('retired_schemas',[])))

for rel in ['schemas/catalog/schema-catalog.csv','api/interface-catalog.csv','registries/registry-entry-catalog.csv']:
    with (ROOT/rel).open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
    required={'repository_release_target','repository_release_target_status','release_status','artifact_lifecycle_state','controlling_published_baseline','baseline_date'}
    check('csv_metadata_columns_'+Path(rel).stem, bool(rows) and required.issubset(rows[0]), sorted(required-set(rows[0]) if rows else required))
    check('csv_metadata_values_'+Path(rel).stem, all(r['repository_release_target']=='v2.0.1' and r['repository_release_target_status']=='UNRELEASED_ACCUMULATED_CORRECTION_SET' and r['release_status']=='PUBLIC_REVIEW_CONTROLLED_BASELINE' and r['artifact_lifecycle_state']=='CURRENT' and r['controlling_published_baseline']=='v2.0.0' and r['baseline_date']=='2026-07-30' for r in rows))

human_files=['schemas/SCHEMA-CATALOG.md','schemas/README.md','api/INTERFACE-CATALOG.md','registries/REGISTRY-ENTRY-CATALOG.md','registries/README.md']
for rel in human_files:
    t=(ROOT/rel).read_text()
    check('human_metadata_'+Path(rel).name, 'CURRENT' in t and 'v2.0.1' in t and 'PUBLIC_REVIEW_CONTROLLED_BASELINE' in t and '2026-07-30' in t, rel)
check('no_active_working_draft', all('Working Draft' not in (ROOT/r).read_text() for r in ['schemas/SCHEMA-CATALOG.md','schemas/README.md','schemas/catalog/schema-catalog.json','schemas/examples/ds003-implementation-metadata-response.json']))

specs=['spec/AGCP-Multitenant-Operational-Specification.md','spec/ledger/AGCP-Append-Only-Governance-Ledger-Specification.md','spec/AGCP-Policy-Evaluation-Contract.md','spec/AGCP-Provenance-Wire-Format-Specification.md','spec/AGCP-Human-Review-Specification.md','spec/AGCP-Error-Mapping.md','spec/AGCP-HTTP-Interface-Specification.md']
for rel in specs:
    head='\n'.join((ROOT/rel).read_text().splitlines()[:20])
    check('spec_header_'+Path(rel).stem, 'Artifact Lifecycle:' in head and 'v2.0.1' in head and 'Unreleased Accumulated Correction Set' in head and 'v2.0.0 Public Review' in head and '2026-07-30' in head, head)

api=yaml.safe_load((ROOT/'api/AGCP-HTTP-Contract.yaml').read_text())
check('openapi_release_metadata', api['info']['version']=='2.0.1' and api.get('x-agcp-specification-release')=='v2.0.1', {'info':api['info']['version'],'extension':api.get('x-agcp-specification-release')})
manifest=yaml.safe_load((ROOT/'conformance/agcp-conformance-manifest.yml').read_text())['agcp_conformance_manifest']
ms=manifest['spec']
check('manifest_release_metadata', ms=={**ms,} and ms.get('repository_release_target')=='v2.0.1' and ms.get('repository_release_target_status')=='unreleased-accumulated-correction-set' and ms.get('artifact_lifecycle_state')=='current' and ms.get('controlling_published_baseline')=='v2.0.0' and ms.get('controlling_baseline_status')=='public-review-controlled-baseline' and str(ms.get('baseline_date'))=='2026-07-30' and ms.get('agcp_release')=='v2.0.1', ms)
check('manifest_registers_policy', 'release_lifecycle_metadata' in manifest)

ex=loadj('schemas/examples/ds003-implementation-metadata-response.json')
r=ex['supported_agcp_releases'][0]; ss=ex['schema_set']
check('ds003_release_metadata', r['release_id']=='AGCP-v2.0.0' and r['specification_version']=='2.0.0' and r['publication_status']=='PUBLISHED' and r['baseline_bundle_publication_status']=='UNPUBLISHED' and r['baseline_bundle_digest']['value']=='790bffe0883c5371c6007986e373e275c9e966cb40c84c8186f38e4365f8c326', r)
check('ds003_schema_set_metadata', ss['schema_set_id']=='DS-SET-v2.0.1' and ss['schema_catalog_id']=='DS-CATALOG-1.0' and ss['catalog_version']=='1.0.50' and ss['agcp_specification_version']=='2.0.1' and ss['publication_status']=='RELEASE_CANDIDATE' and ss['schemas'][0]['lifecycle_state']=='Implemented', {k:ss.get(k) for k in ['schema_set_id','schema_catalog_id','catalog_version','agcp_specification_version','publication_status']})

for rel in ['registries/constraint-type-registry.json','registries/invariant-type-registry.json','registries/rejection-code-registry.json']:
    d=loadj(rel); rr=d['release']; lc=d['lifecycle']
    check('registry_metadata_'+Path(rel).stem, rr['specification_version']==rr['registry_release'] and rr['publication_status']=='CURRENT' and lc['lifecycle_state']=='ACTIVE', {'release':rr,'lifecycle':lc})
    x=copy.deepcopy(d); declared=x['integrity'].pop('document_digest')['value']
    check('registry_digest_'+Path(rel).stem, declared==dig(x), {'declared':declared,'computed':dig(x)})

notes=(ROOT/'RELEASE_NOTES_v2.0.1.md').read_text()
check('release_notes_metadata', all(x in notes[:600] for x in ['Unreleased accumulated correction set','CURRENT','PUBLIC_REVIEW_CONTROLLED_BASELINE','2026-07-30']))
check('release_notes_current_profile', '2.0.0-draft.6' in notes and '3e391cd0b0a89189434776c4593dedb2b3dd460bfd5fe7f89d8fc8fdb4373b2d' in notes)

for rel in report_files:
    d=loadj(rel)
    check('report_release_context_'+Path(rel).stem, d.get('release_context')==ctx, d.get('release_context'))

source_files=[POLICY_PATH,'governance/AGCP-Release-Lifecycle-Metadata-Policy.md','schemas/catalog/schema-catalog.json','schemas/catalog/schema-catalog.csv','schemas/SCHEMA-CATALOG.md','schemas/README.md','api/interface-catalog.json','api/interface-catalog.csv','api/INTERFACE-CATALOG.md','registries/registry-entry-catalog.json','registries/registry-entry-catalog.csv','registries/REGISTRY-ENTRY-CATALOG.md','registries/constraint-type-registry.json','registries/invariant-type-registry.json','registries/rejection-code-registry.json','schemas/examples/ds003-implementation-metadata-response.json','conformance/http/AGCP-HTTP-Error-Metadata-Test-Vectors.json','api/AGCP-HTTP-Contract.yaml','conformance/agcp-conformance-manifest.yml','RELEASE_NOTES_v2.0.1.md','governance/validate_release_lifecycle_metadata.py',]+specs
report={'release_context':ctx,'report_id':'AGCP-P2-01-RELEASE-LIFECYCLE-METADATA','status':'PASS' if not issues else 'FAIL','validated_at':'2026-08-03','finding':'P2-01','catalog_versions':{'schema':'1.0.50','interface':'1.0.5','registry':'1.0.3'},'specification_count':len(specs),'validation_report_count':len(report_files),'source_hashes':{r:sha(r) for r in source_files},'checks':checks,'issues':issues}
(ROOT/'governance/AGCP-release-lifecycle-metadata-validation.json').write_text(json.dumps(report,indent=2,default=str)+'\n')
print(json.dumps({'status':report['status'],'checks':len(checks),'issues':issues},indent=2,default=str))
sys.exit(0 if not issues else 1)
