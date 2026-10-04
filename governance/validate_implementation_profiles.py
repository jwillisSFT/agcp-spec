#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json

from release_version import release_context


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(); p.add_argument('--repo',default='.'); p.add_argument('--report'); a=p.parse_args(); root=Path(a.repo).resolve()
    issues=[]
    cat=json.loads((root/'implementer/implementation-profile-catalog.json').read_text())
    if cat.get('catalog_version')!='2.0.0': issues.append('catalog_version must be 2.0.0')
    entries=cat.get('entries',[])
    if not any(e.get('profile_id')=='AGCP-FULL-SCOPE-MULTITENANT-EXAMPLE-PROFILE' for e in entries): issues.append('missing public example profile')
    schema=json.loads((root/'implementer/AGCP-Implementation-Profile-Schema.json').read_text())
    if schema['properties']['document']['properties']['format_version'].get('const')!='2.0.0': issues.append('implementation profile schema format mismatch')
    for required in ['AGCP-Identity-and-Authorization-Store-Profile-Specification.md','AGCP-Identity-and-Authorization-Store-Profile-Schema.json','AGCP-Identity-and-Authorization-Store-Profile-Template.md','AGCP-PEP-Profile-Specification.md','AGCP-PEP-Profile-Schema.json','AGCP-PEP-Profile-Template.md']:
        if not (root/'implementer'/required).is_file(): issues.append('missing:'+required)
    man=json.loads((root/'implementer/implementation-profile-manifest.json').read_text())
    for e in man.get('files',[]):
        f=root/'implementer'/e['path']
        if not f.is_file() or sha(f)!=e['sha256'] or f.stat().st_size!=e['bytes']: issues.append('manifest mismatch:'+e['path'])
    # generic-boundary scan for prohibited public-profile vocabulary
    prohibited=['student','coder','team workspace','class delivery','vps-']
    scan=['AGCP-Implementation-Profile-Specification.md','AGCP-Implementation-Profile-Template.md','AGCP-Implementation-Profile-Schema.json']
    for rel in scan:
        s=(root/'implementer'/rel).read_text().lower()
        for token in prohibited:
            if token in s: issues.append(f'generic profile contamination:{rel}:{token}')
    report={'release_context':release_context(),'validation_type':'AGCP_PUBLIC_IMPLEMENTATION_PROFILE_ARTIFACT_VALIDATION','status':'PASS' if not issues else 'FAIL','profile_format_version':'2.0.0','informational_examples_checked':len(entries),'manifest_files_checked':len(man.get('files',[])),'issues':issues}
    out=json.dumps(report,indent=2)+'\n'
    target=Path(a.report) if a.report else root/'governance/AGCP-implementation-profile-validation.json'; target.write_text(out)
    print(out,end=''); return 0 if not issues else 1
if __name__=='__main__': raise SystemExit(main())
