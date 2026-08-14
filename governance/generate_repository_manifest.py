#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from datetime import date
from release_version import ROOT, SYNC_MANIFEST, SYNC_REPORT, INTEGRITY_REPORT, RELEASE_TAG, RELEASE_STATUS, BASELINE_DATE, ARTIFACT_LIFECYCLE_STATE, release_context

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
out=ROOT/SYNC_MANIFEST
exclusions={SYNC_MANIFEST,SYNC_REPORT,INTEGRITY_REPORT}
files=[]
for p in sorted(ROOT.rglob("*")):
    if not p.is_file() or ".git" in p.parts: continue
    rel=p.relative_to(ROOT).as_posix()
    if rel in exclusions: continue
    files.append({"path":rel,"sha256":sha(p),"bytes":p.stat().st_size})
report={"release_context":release_context(),"manifest_type":"AGCP_REPOSITORY_SYNCHRONIZATION_MANIFEST","manifest_version":"1.1.0","version_source":"VERSION","repository_release_target":RELEASE_TAG,"repository_release_target_status":RELEASE_STATUS,"controlling_published_baseline":RELEASE_TAG,"controlling_baseline_status":RELEASE_STATUS,"baseline_date":BASELINE_DATE,"artifact_lifecycle_state":ARTIFACT_LIFECYCLE_STATE,"generated_date":str(date.today()),"scope_exclusions":sorted(exclusions),"file_count":len(files),"files":files}
out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({"status":"PASS","manifest":SYNC_MANIFEST,"file_count":len(files)},indent=2))
