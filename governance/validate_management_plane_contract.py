#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import copy, json, sys, yaml
from jsonschema import Draft202012Validator, RefResolver
from release_version import ROOT, SEMVER, RELEASE_TAG, release_context

checks=[]; issues=[]
def ck(name,ok,detail=None):
    checks.append({"check":name,"status":"PASS" if ok else "FAIL","detail":detail})
    if not ok: issues.append(f"{name}: {detail}")
def loadj(r): return json.loads((ROOT/r).read_text(encoding="utf-8"))

def validator_for(srel):
    s=loadj(srel)
    store={}
    for p in (ROOT/"schemas").glob("*.json"):
        try:
            x=json.loads(p.read_text(encoding="utf-8")); store[x.get("$id",p.as_uri())]=x
        except Exception: pass
    resolver=RefResolver(base_uri=(ROOT/srel).as_uri(),referrer=s,store=store)
    return s,Draft202012Validator(s,resolver=resolver)

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
fixture_errors=[]
for srel,erel in fixtures:
    try:
        s,v=validator_for(srel); e=loadj(erel); errs=list(v.iter_errors(e))
        if errs: fixture_errors.append([erel,[x.message for x in errs[:5]]])
    except Exception as ex: fixture_errors.append([erel,[str(ex)]])
ck("management_examples_validate",not fixture_errors,fixture_errors)

d47=loadj("schemas/management_capabilities_response.json")
d50=loadj("schemas/test_control_request.json"); d51=loadj("schemas/test_control_result.json")
ctl=set(d50["properties"]["control_type"]["enum"]); ctlr=set(d51["properties"]["control_type"]["enum"])
needed={"TARGET_EXECUTION_FIXTURE","ENFORCEMENT_PATH_FAULT_FIXTURE"}
ck("new_controls_are_symmetric",needed<=ctl and ctl==ctlr,{"request_only":sorted(ctl-ctlr),"result_only":sorted(ctlr-ctl)})

# Wire contract and safety invariants.
ck("test_control_wire_versions",d50.get("properties",{}).get("control_version",{}).get("const")=="1.2" and d51.get("properties",{}).get("result_version",{}).get("const")=="1.2",
   {"DS-050":d50.get("properties",{}).get("control_version"),"DS-051":d51.get("properties",{}).get("result_version")})
ck("ds051_required_management_readback",{"runtime_binding_status","requested_by"}<=set(d51.get("required",[])) and all(x in d51.get("properties",{}) for x in ["tenant_id","governance_domain","expires_at"]),
   {"required":d51.get("required",[])})

# Validate semantic schema invariants using negative and positive instances rather than only text inspection.
_,v50=validator_for("schemas/test_control_request.json")
base50=loadj("schemas/examples/ds050-test-control-request.json")
no_exp=copy.deepcopy(base50); no_exp.pop("expires_at",None)
reset={
  "operation_id":"tcop-reset","control_version":"1.2","test_scope":"scope-reset","control_type":"RESET_TEST_SCOPE",
  "requested_by":{"principal_id":"harness"},"reason":"cleanup","test_only":True,
  "request_digest":"0"*64
}
ck("non_reset_controls_require_finite_lease",bool(list(v50.iter_errors(no_exp))) and not list(v50.iter_errors(reset)),
   {"non_reset_without_expiry_error_count":len(list(v50.iter_errors(no_exp))),"reset_without_expiry_error_count":len(list(v50.iter_errors(reset)))})

_,v51=validator_for("schemas/test_control_result.json")
base51=loadj("schemas/examples/ds051-test-control-result.json")
unbound=copy.deepcopy(base51); unbound["runtime_binding_status"]="RECORD_ONLY"
no_principal=copy.deepcopy(base51); no_principal.pop("requested_by",None)
no_result_exp=copy.deepcopy(base51); no_result_exp.pop("expires_at",None)
ck("effective_implies_bound",bool(list(v51.iter_errors(unbound))),[e.message for e in list(v51.iter_errors(unbound))[:3]])
ck("result_requires_applying_principal",bool(list(v51.iter_errors(no_principal))),[e.message for e in list(v51.iter_errors(no_principal))[:3]])
ck("accepted_non_reset_result_preserves_expiry",bool(list(v51.iter_errors(no_result_exp))),[e.message for e in list(v51.iter_errors(no_result_exp))[:3]])

# Capability discovery: exact variants + collection recovery support.
cap=loadj("schemas/examples/ds047-management-capabilities-response.json")
advertised={x.get("control_type"):x for x in cap.get("test_control_capabilities",[])}
ck("new_controls_discoverable",needed<=set(advertised),sorted(advertised))
ck("test_control_enumeration_discoverable",d47.get("properties",{}).get("response_version",{}).get("const")=="1.1" and "test_control_enumeration_supported" in d47.get("required",[]) and cap.get("test_control_enumeration_supported") is True,
   {"response_version":d47.get("properties",{}).get("response_version"),"example":cap.get("test_control_enumeration_supported")})
target=advertised.get("TARGET_EXECUTION_FIXTURE",{}).get("supported_control_parameters",{})
fault=advertised.get("ENFORCEMENT_PATH_FAULT_FIXTURE",{}).get("supported_control_parameters",{})
ck("test_control_variants_discoverable",
   bool(target.get("execution_modes")) and bool(target.get("terminal_outcomes")) and isinstance(target.get("virtual_time_release_supported"),bool) and bool(fault.get("fault_targets")) and bool(fault.get("fault_modes")) and bool(fault.get("injection_points")),
   {"target":target,"fault":fault})

# IF-005 collection enumeration and required filters.
collection=contract.get("paths",{}).get("/agcp/test/v1/controls",{})
getop=collection.get("get")
expected_filters={"test_scope","tenant_id","governance_domain","control_type","effect_status","consumption_status","cleanup_required"}
actual_filters={x.get("name") for x in (getop or {}).get("parameters",[]) if x.get("in")=="query"}
ck("if005_collection_readback",bool(getop) and getop.get("operationId")=="listConformanceTestControls" and expected_filters<=actual_filters,
   {"operationId":(getop or {}).get("operationId"),"filters":sorted(actual_filters)})
post_desc=collection.get("post",{}).get("responses",{}).get("200",{}).get("description","")
ck("if005_post_requires_bound_and_effective_semantics","runtime_binding_status=BOUND" in post_desc and "effect_status=EFFECTIVE" in post_desc,post_desc)

mp=yaml.safe_load((ROOT/"conformance/AGCP-Management-Plane-Harness-Spec.yml").read_text())
ids={x["id"] for x in mp.get("checks",[])}
ck("management_harness_negative_paths",{"MP-TC-005","MP-TC-006","MP-TC-007","MP-TC-009","MP-TC-010"}<=ids,sorted(ids))
ck("management_harness_control_plane_operability",{"MP-CAP-002","MP-TC-011","MP-TC-012","MP-TC-013"}<=ids,sorted(ids))

report={"release_context":release_context(),"validation_type":"AGCP_MANAGEMENT_PLANE_CONTRACT","status":"PASS" if not issues else "FAIL","checks":checks,"issues":issues}
(ROOT/"governance/AGCP-management-plane-contract-validation.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps({"status":report["status"],"checks":len(checks),"issues":issues},indent=2)); raise SystemExit(0 if not issues else 1)
