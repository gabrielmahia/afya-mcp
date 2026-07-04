"""AfyaMCP — Kenya Health System Navigation (6 tools). All data DEMO."""
from __future__ import annotations
from typing import Optional
from fastmcp import FastMCP

mcp = FastMCP(name="afya-mcp", instructions="Kenya health system navigation. DEMO data only.")

NHIF_BENEFITS = {
    "outpatient": "NHIF SHA covers outpatient at accredited facilities. Annual limit varies by contribution tier.",
    "inpatient":  "Inpatient coverage up to 180 days per year. Shared rooms covered; private rooms may attract a top-up.",
    "maternity":  "Normal delivery: KES 10,000. C-section: KES 30,000. Accredited facilities only.",
    "dental":     "Basic dental covered biannually at accredited dental clinics.",
    "optical":    "Optical covered annually — frames and lenses up to KES 5,000.",
    "chronic":    "Chronic disease management covered under SHA Enhancement Fund for specific conditions.",
    "dialysis":   "Renal dialysis covered at designated centres under SHA.",
}

FACILITY_LEVELS = {
    "dispensary": "Level 2 — basic outpatient, maternal, immunisation",
    "health_centre": "Level 3 — outpatient, inpatient beds, minor surgery",
    "sub_county_hospital": "Level 4 — general surgery, lab, radiology",
    "county_hospital": "Level 5 — specialist services, ICU",
    "national_referral": "Level 6 — Kenya National Hospital, Kenyatta, Moi Teaching",
}

@mcp.tool(name="nhif_coverage_query", description="Query NHIF/SHA coverage for a procedure or condition. DEMO.")
def nhif_coverage_query(query: str, member_tier: Optional[str] = "standard") -> dict:
    q = query.lower()
    matched = {k: v for k, v in NHIF_BENEFITS.items() if k in q or any(w in q for w in k.split("_"))}
    if not matched:
        matched = {"general": "NHIF SHA covers most inpatient and outpatient services at accredited facilities."}
    return {"source": "DEMO — verify at nhif.or.ke or sha.go.ke", "query": query,
            "member_tier": member_tier, "coverage": matched,
            "tip": "Always confirm coverage before procedure. Call SHA: 0800720601 (free)."}

@mcp.tool(name="health_facility_finder", description="Find accredited health facilities in a Kenya county/sub-county. DEMO.")
def health_facility_finder(county: str, level: Optional[str] = None, nhif_only: Optional[bool] = True) -> dict:
    sample = [
        {"name": f"{county} County Referral Hospital", "level": "county_hospital", "nhif_accredited": True, "county": county},
        {"name": f"{county} Sub-County Hospital", "level": "sub_county_hospital", "nhif_accredited": True, "county": county},
        {"name": f"Central Health Centre — {county}", "level": "health_centre", "nhif_accredited": nhif_only, "county": county},
        {"name": f"Community Dispensary — {county}", "level": "dispensary", "nhif_accredited": False, "county": county},
    ]
    if level:
        sample = [f for f in sample if level.lower() in f["level"]]
    if nhif_only:
        sample = [f for f in sample if f["nhif_accredited"]]
    return {"source": "DEMO — verify at KenyaEMR/DHIS2", "county": county,
            "facilities": sample, "tip": "For real-time facility data: ehealth.go.ke"}

@mcp.tool(name="chw_service_lookup", description="Lookup CHW services in a Kenya sub-county. DEMO.")
def chw_service_lookup(sub_county: str) -> dict:
    return {"source": "DEMO", "sub_county": sub_county,
            "chw_services": ["Health education","Malaria prevention","Maternal-child health","Immunisation referral",
                             "TB contact tracing","Nutrition screening","NCDs follow-up"],
            "referral_pathway": "CHW → Health Centre → Sub-County Hospital → County Referral",
            "contact": "Contact your county health department for CHW assignment in your village."}

@mcp.tool(name="maternal_health_guide", description="ANC milestones, danger signs, and delivery guidance for Kenya. DEMO.")
def maternal_health_guide(trimester: str, specific_concern: Optional[str] = None) -> dict:
    GUIDE = {
        "first": {"anc_visits": "At least 1 visit before 12 weeks", "key_tests": ["Blood group","Hemoglobin","HIV test","Syphilis screening"],
                  "danger_signs": ["Heavy bleeding","Severe vomiting","Fever above 38°C"]},
        "second": {"anc_visits": "2 visits (20 and 26 weeks)", "key_tests": ["Ultrasound","Glucose screening","Tetanus toxoid"],
                   "danger_signs": ["Reduced fetal movement","Severe headache","Visual disturbances"]},
        "third": {"anc_visits": "2 visits (32 and 36 weeks)", "key_tests": ["Presentation check","Birth plan review"],
                  "danger_signs": ["Labour before 37 weeks","Absence of fetal movement","Severe swelling"]},
    }
    t = trimester.lower().replace("1st","first").replace("2nd","second").replace("3rd","third")
    data = GUIDE.get(t, GUIDE["first"])
    return {"source": "DEMO — verify with qualified midwife/obstetrician", "trimester": trimester,
            **data, "nhif_maternity": "Deliver at NHIF-accredited facility. Normal delivery: KES 10,000 covered."}

@mcp.tool(name="essential_medicines", description="Query Kenya Essential Medicines List. DEMO.")
def essential_medicines(query: str) -> dict:
    COMMON = {"amoxicillin": "Tier 1 — dispensary level. Generic available. Avg KES 50/course.",
               "metformin":   "Tier 2 — health centre. Generic available. Avg KES 30/month.",
               "paracetamol": "Tier 1 — all facilities. OTC available. Avg KES 10/strip.",
               "malaria":     "Artemether-lumefantrine (Coartem) — Tier 1, free at public facilities.",
               "tb":          "First-line TB drugs — free through NTLD programme at public facilities.",
               "insulin":     "Tier 3 — sub-county hospital and above. NHIF covers with chronic disease card."}
    q = query.lower()
    match = next((v for k, v in COMMON.items() if k in q), "Not in sample dataset — check EML at kemsa.go.ke")
    return {"source": "DEMO — Kenya Essential Medicines List 2024", "query": query,
            "information": match, "kemsa": "kemsa.go.ke", "disclaimer": "Consult a pharmacist or prescriber."}

@mcp.tool(name="health_rights_query", description="Patient rights under Kenya Health Act 2017. DEMO.")
def health_rights_query(topic: str) -> dict:
    RIGHTS = {
        "consent":         "Informed consent required before any procedure. Patient may refuse treatment.",
        "privacy":         "Medical records are confidential. Cannot be shared without consent (HIV Act, Data Protection Act).",
        "emergency":       "Any public facility must provide emergency care regardless of ability to pay.",
        "second_opinion":  "Patient has the right to seek a second opinion from another provider.",
        "complaint":       "File complaints: Kenya Medical Practitioners and Dentists Council (KMPDC), or county health department.",
        "nhif_dispute":    "NHIF disputes: SHA Ombudsman — 0800720601. Must be resolved within 30 days.",
    }
    t = topic.lower()
    matched = {k: v for k, v in RIGHTS.items() if k in t or any(w in t for w in k.split("_"))}
    return {"source": "DEMO — Kenya Health Act 2017", "topic": topic,
            "rights": matched or {"general": "Review Kenya Health Act 2017 at kenyalaw.org"},
            "all_topics": list(RIGHTS.keys()), "disclaimer": "Not legal or medical advice."}

def main() -> None:
    """Console entry point."""
    mcp.run()
