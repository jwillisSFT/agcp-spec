#!/usr/bin/env python3
"""Refresh existing source_hashes entries in controlled JSON reports."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
from release_version import ROOT, RELEASE_TAG, SYNC_MANIFEST, SYNC_REPORT, INTEGRITY_REPORT

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
EXCLUDE={SYNC_MANIFEST,SYNC_REPORT,INTEGRITY_REPORT,"governance/AGCP-version-source-validation.json","governance/AGCP-normative-statement-inventory-validation.json"}
changed=[]
for path in sorted(ROOT.rglob("*.json")):
    rel=path.relative_to(ROOT).as_posix()
    if rel in EXCLUDE: continue
    try: obj=json.loads(path.read_text(encoding="utf-8"))
    except Exception: continue
    # Historical release reports are immutable records. Their embedded hashes refer
    # to the source state that existed for that historical release and MUST NOT be
    # rewritten to match the current repository.
    if isinstance(obj, dict):
        rc = obj.get("release_context")
        if isinstance(rc, dict):
            historical_target = rc.get("repository_release_target") or rc.get("controlling_published_baseline")
            if isinstance(historical_target, str) and historical_target.startswith("v") and historical_target != RELEASE_TAG:
                continue
    dirty=[False]
    def walk(x):
        if isinstance(x,dict):
            sh=x.get("source_hashes")
            if isinstance(sh,dict):
                for rp,hv in list(sh.items()):
                    p=ROOT/rp
                    if p.is_file() and isinstance(hv,str) and len(hv)==64:
                        new=sha(p)
                        if new!=hv: sh[rp]=new; dirty[0]=True
            for v in x.values(): walk(v)
        elif isinstance(x,list):
            for v in x: walk(v)
    walk(obj)
    if dirty[0]: path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"); changed.append(rel)
print(json.dumps({"status":"PASS","files_updated":changed},indent=2))
