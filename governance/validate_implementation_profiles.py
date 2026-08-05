#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, sys

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
 p=argparse.ArgumentParser(); p.add_argument('--repo',default='.'); p.add_argument('--report'); a=p.parse_args(); root=Path(a.repo).resolve()
 issues=[]
 cat=json.loads((root/'implementer/implementation-profile-catalog.json').read_text())
 entries=cat.get('entries',[])
 if len(entries)!=1 or entries[0].get('profile_id')!='AGCP-FULL-SCOPE-MULTITENANT-EXAMPLE-PROFILE': issues.append('unexpected public catalog entries')
 man=json.loads((root/'implementer/implementation-profile-manifest.json').read_text())
 for e in man.get('files',[]):
  f=root/'implementer'/e['path']
  if not f.is_file() or sha(f)!=e['sha256'] or f.stat().st_size!=e['bytes']: issues.append('manifest mismatch:'+e['path'])
 report={'release_context':{'repository_release_target':'v2.0.4','repository_release_target_status':'PUBLIC_REVIEW_CONTROLLED_BASELINE','controlling_published_baseline':'v2.0.4','controlling_baseline_status':'PUBLIC_REVIEW_CONTROLLED_BASELINE','baseline_date':'2026-08-05','artifact_lifecycle_state':'CURRENT'},'validation_type':'AGCP_PUBLIC_IMPLEMENTATION_PROFILE_ARTIFACT_VALIDATION','status':'PASS' if not issues else 'FAIL','validated_at':'2026-08-05','controlled_profiles_published':0,'informational_examples_checked':1,'manifest_files_checked':len(man.get('files',[])),'manifest_sha256':sha(root/'implementer/implementation-profile-manifest.json'),'issues':issues}
 out=json.dumps(report,indent=2)+'\n'
 if a.report: Path(a.report).write_text(out)
 else: (root/'governance/AGCP-implementation-profile-validation.json').write_text(out)
 print(out,end=''); return 0 if not issues else 1
if __name__=='__main__': raise SystemExit(main())
