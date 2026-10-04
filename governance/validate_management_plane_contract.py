#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json, sys, yaml
from jsonschema import Draft202012Validator, RefResolver
from release_version import ROOT, SEMVER, RELEASE_TAG, release_context

checks=[]; issues=[]
def ck(name,ok,detail=None):
    checks.append({"check":name,"status":"PASS" if ok else "FAIL","detail":detail})
    if not ok: issues.append(f"{name}: {detail}")
def loadj(r): return json.loads((ROOT/r).read_text(encoding="utf-8"))

contract=yaml.safe_load((ROOT/"api/AGCP-Management-Contract.yaml").read_text(encoding="utf-8"))
ck("management_openapi_release",contract.get("info",{}).get("version")==SEMVER and contract.get("x-agcp-specification-release")==RELEASE_TAG,{"info.version":contract.get("info",{}).get("version"),"release":contract.get("x-agcp-specification-release")})
refs=[]
def walk(x):
    if isinstance(x,dict):
        if isinstance(x.get("$ref"),str) and x["$ref"].startswith("../schemas/"): refs.append(x["$ref"])
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(contract)
missing=[r for r in refs if not (ROOT/"api"/r).resolve().is_file()]
ck("management_openapi_refs_resolve",not missing,missing)

fixtures=[
 ("schemas/governance_observation_event.json","schemas/examples/ds046-governance-observation-event.json"),
 ("schemas/management_capabilities_response.json","schemas/examples/ds047-management-capabilities-response.json"),
 ("schemas/governance_actuation_request.json","schemas/examples/ds048-governance-actuation-request.json"),
 ("schemas/governance_actuation_result.json","schemas/examples/ds049-governance-actuation-result.json"),
 ("schemas/test_control_request.json","schemas/examples/ds050-test-control-request.json"),
 ("schemas/test_control_result.json","schemas/examples/ds051-test-control-result.json"),
]
store={}
for p in (ROOT/"schemas").glob("*.json"):
    try:
        s=json.loads(p.read_text()); store[s.get("$id",p.as_uri())]=s
    except Exception: pass
fixture_errors=[]
for srel,erel in fixtures:
    try:
        s=loadj(srel); e=loadj(erel); resolver=RefResolver(base_uri=(ROOT/srel).as_uri(),referrer=s,store=store); errs=list(Draft202012Validator(s,resolver=resolver).iter_errors(e))
        if errs: fixture_errors.append([erel,[x.message for x in errs[:5]]])
    except Exception as ex: fixture_errors.append([erel,[str(ex)]])
ck("management_examples_validate",not fixture_errors,fixture_errors)

d50=loadj("schemas/test_control_request.json"); d51=loadj("schemas/test_control_result.json"); ctl=set(d50["properties"]["control_type"]["enum"]); ctlr=set(d51["properties"]["control_type"]["enum"])
needed={"TARGET_EXECUTION_FIXTURE","ENFORCEMENT_PATH_FAULT_FIXTURE"}
ck("new_controls_are_symmetric",needed<=ctl and ctl==ctlr,{"request_only":sorted(ctl-ctlr),"result_only":sorted(ctlr-ctl)})
cap=loadj("schemas/examples/ds047-management-capabilities-response.json"); advertised={x.get("control_type") for x in cap.get("test_control_capabilities",[])}
ck("new_controls_discoverable",needed<=advertised,sorted(advertised))
mp=yaml.safe_load((ROOT/"conformance/AGCP-Management-Plane-Harness-Spec.yml").read_text()); ids={x["id"] for x in mp.get("checks",[])}
ck("management_harness_negative_paths",{"MP-TC-005","MP-TC-006","MP-TC-007","MP-TC-009","MP-TC-010"}<=ids,sorted(ids))
report={"release_context":release_context(),"validation_type":"AGCP_MANAGEMENT_PLANE_CONTRACT","status":"PASS" if not issues else "FAIL","checks":checks,"issues":issues}
(ROOT/"governance/AGCP-management-plane-contract-validation.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps({"status":report["status"],"checks":len(checks),"issues":issues},indent=2)); raise SystemExit(0 if not issues else 1)
