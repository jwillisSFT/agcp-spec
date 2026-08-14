#!/usr/bin/env python3
"""Synchronize current AGCP release metadata from the root VERSION file."""
from __future__ import annotations
import argparse, csv, json, re, sys
from pathlib import Path
import yaml
from openpyxl import load_workbook
from release_version import (ROOT, SEMVER, RELEASE_TAG, RTM_SPEC_VERSION, RELEASE_IDENTIFIER,
    CURRENT_RELEASE_NOTES, RELEASE_STATUS, BASELINE_DATE, ARTIFACT_LIFECYCLE_STATE,
    SETTINGS, release_context, release_lifecycle_metadata)

REPORT = ROOT / "governance/AGCP-version-source-validation.json"

def write_text_if_changed(path: Path, text: str) -> bool:
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old == text: return False
    path.write_text(text, encoding="utf-8"); return True

def sync(write: bool) -> tuple[list[str], list[str]]:
    changed=[]; issues=[]
    # Machine-readable lifecycle metadata is generated from VERSION.
    meta_path=ROOT/"governance/release-lifecycle-metadata.json"
    desired=json.dumps(release_lifecycle_metadata(),indent=2,ensure_ascii=False)+"\n"
    if (not meta_path.exists()) or meta_path.read_text(encoding="utf-8") != desired:
        changed.append(meta_path.relative_to(ROOT).as_posix())
        if write: meta_path.write_text(desired,encoding="utf-8")

    # OpenAPI current release metadata. Preserve source formatting and patch only
    # the controlled current-release fields.
    api_path=ROOT/"api/AGCP-HTTP-Contract.yaml"; api_text=api_path.read_text(encoding="utf-8")
    updated=re.sub(r"(?m)^(  version:)\s*[^\n]+$", rf"\1 {SEMVER}", api_text, count=1)
    updated=re.sub(r"(?m)^(x-agcp-specification-release:)\s*[^\n]+$", rf"\1 {RELEASE_TAG}", updated, count=1)
    if updated != api_text:
        changed.append(api_path.relative_to(ROOT).as_posix())
        if write: api_path.write_text(updated,encoding="utf-8")

    # Conformance manifest release identity. Preserve formatting; generated values
    # are injected only into the current-release metadata block.
    man_path=ROOT/"conformance/agcp-conformance-manifest.yml"; man_text=man_path.read_text(encoding="utf-8")
    updated=man_text
    replacements={
      "repository_release_target": RELEASE_TAG,
      "repository_release_target_status": RELEASE_STATUS.lower().replace("_","-"),
      "artifact_lifecycle_state": ARTIFACT_LIFECYCLE_STATE.lower(),
      "controlling_published_baseline": RELEASE_TAG,
      "controlling_baseline_status": RELEASE_STATUS.lower().replace("_","-"),
      "baseline_date": BASELINE_DATE,
      "agcp_release": RELEASE_TAG,
    }
    lines=updated.splitlines(True); in_spec=False
    for i,line in enumerate(lines):
        if line.startswith("  spec:"): in_spec=True; continue
        if in_spec and line.startswith("  ") and not line.startswith("    "): break
        if in_spec:
            m=re.match(r"(    ([A-Za-z0-9_]+):)\s*.*?(\r?\n)?$",line)
            if m and m.group(2) in replacements:
                nl=m.group(3) or ""; lines[i]=f"    {m.group(2)}: {replacements[m.group(2)]}{nl}"
    updated="".join(lines)
    if not re.search(r"(?m)^    version_source: VERSION$", updated):
        updated=updated.replace("    release_model: repository_release\n","    release_model: repository_release\n    version_source: VERSION\n",1)
    if updated != man_text:
        changed.append(man_path.relative_to(ROOT).as_posix())
        if write: man_path.write_text(updated,encoding="utf-8")

    # RTM specification version is injected into every controlled CR row and disposition row.
    rtm_path=ROOT/"spec/AGCP_Requirements_Traceability_Matrix_(RTM).xlsx"
    wb=load_workbook(rtm_path,data_only=False); ws=wb[wb.sheetnames[0]]
    hdr={ws.cell(1,c).value:c for c in range(1,ws.max_column+1)}; modified=False
    for r in range(2,ws.max_row+1):
        if ws.cell(r,hdr["Specification_Version"]).value != RTM_SPEC_VERSION:
            ws.cell(r,hdr["Specification_Version"]).value=RTM_SPEC_VERSION; modified=True
    if "NS_Inventory_Dispositions" in wb.sheetnames:
        ds=wb["NS_Inventory_Dispositions"]; dh={ds.cell(1,c).value:c for c in range(1,ds.max_column+1)}
        if "Specification_Version" in dh:
            for r in range(2,ds.max_row+1):
                if ds.cell(r,dh["Specification_Version"]).value != RTM_SPEC_VERSION:
                    ds.cell(r,dh["Specification_Version"]).value=RTM_SPEC_VERSION; modified=True
    if modified:
        changed.append(rtm_path.relative_to(ROOT).as_posix())
        if write: wb.save(rtm_path)

    # Current release notes are human-authored but must be VERSION-derived in filename and header.
    notes=ROOT/CURRENT_RELEASE_NOTES
    if not notes.is_file(): issues.append(f"missing current release notes: {CURRENT_RELEASE_NOTES}")
    elif RELEASE_TAG not in notes.read_text(encoding="utf-8")[:1200]: issues.append(f"current release notes header does not identify {RELEASE_TAG}")

    return changed,issues

def validate() -> tuple[list[dict],list[str]]:
    checks=[]; issues=[]
    def ck(name,ok,detail=None):
        checks.append({"check":name,"status":"PASS" if ok else "FAIL","detail":detail})
        if not ok: issues.append(f"{name}: {detail}")
    meta=json.loads((ROOT/"governance/release-lifecycle-metadata.json").read_text(encoding="utf-8"))
    ck("authoritative_version_source", (ROOT/"VERSION").read_text().strip()==SEMVER and meta.get("version_source")=="VERSION", {"VERSION":SEMVER,"metadata_version_source":meta.get("version_source")})
    ck("release_metadata_generated_from_version", meta.get("repository_release_target")==RELEASE_TAG and meta.get("current_repository_specification_version")==SEMVER and meta.get("controlling_published_baseline",{}).get("release_id")==RELEASE_IDENTIFIER, meta)
    api=yaml.safe_load((ROOT/"api/AGCP-HTTP-Contract.yaml").read_text(encoding="utf-8")); ck("openapi_version",api.get("info",{}).get("version")==SEMVER and api.get("x-agcp-specification-release")==RELEASE_TAG,{"info.version":api.get("info",{}).get("version"),"release":api.get("x-agcp-specification-release")})
    man=yaml.safe_load((ROOT/"conformance/agcp-conformance-manifest.yml").read_text(encoding="utf-8"))["agcp_conformance_manifest"]["spec"]; ck("conformance_manifest_version",man.get("version_source")=="VERSION" and man.get("repository_release_target")==RELEASE_TAG and man.get("controlling_published_baseline")==RELEASE_TAG and man.get("agcp_release")==RELEASE_TAG,man)
    wb=load_workbook(ROOT/"spec/AGCP_Requirements_Traceability_Matrix_(RTM).xlsx",data_only=False); ws=wb[wb.sheetnames[0]]; h={ws.cell(1,c).value:c for c in range(1,ws.max_column+1)}; vals={ws.cell(r,h["Specification_Version"]).value for r in range(2,ws.max_row+1)}; ck("rtm_specification_version",vals=={RTM_SPEC_VERSION},sorted(str(v) for v in vals))
    ck("current_release_notes_present",(ROOT/CURRENT_RELEASE_NOTES).is_file(),CURRENT_RELEASE_NOTES)
    # Validator code may import derived constants but must not independently assign the current version.
    offenders=[]
    assign=re.compile(r"^\s*[A-Z_]*(?:VERSION|RELEASE)[A-Z_]*\s*=\s*[\"'](?:v\.?)?"+re.escape(SEMVER)+r"[\"']",re.M)
    for p in sorted((ROOT/"governance").glob("*.py")):
        if p.name in {"release_version.py"}: continue
        if assign.search(p.read_text(encoding="utf-8")): offenders.append(p.relative_to(ROOT).as_posix())
    ck("python_validators_do_not_maintain_independent_release_version",not offenders,offenders)
    return checks,issues

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
    changed,preissues=sync(a.write)
    if a.write:
        # Re-read generated state for validation.
        pass
    checks,issues=validate(); issues=preissues+issues
    report={"release_context":release_context(),"validation_type":"AGCP_SINGLE_SOURCE_VERSION_VALIDATION","status":"PASS" if not issues else "FAIL","version_source":"VERSION","semantic_version":SEMVER,"release_tag":RELEASE_TAG,"rtm_specification_version":RTM_SPEC_VERSION,"synchronization":{"files_requiring_update":changed},"checks":checks,"issues":issues}
    if a.write or a.check: REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
    print(json.dumps({"status":report["status"],"changed":changed,"issues":issues},indent=2,default=str))
    return 0 if not issues else 1
if __name__=="__main__": raise SystemExit(main())
