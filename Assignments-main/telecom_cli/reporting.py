import json
from datetime import datetime
from pathlib import Path

from fraud import is_suspicious
from rating import compute_cost


def build_report(subscribers: dict, cdrs: list, rejected_records: list[str]) -> dict:
    """Create billing, fraud, and data-quality insights from valid CDRs."""
    subscriber_summaries = {
        msisdn: {
            "plan_type": subscriber.plan_type,
            "call_count": 0,
            "total_duration_sec": 0,
            "total_cost": 0.0,
            "suspicious_call_count": 0,
        }
        for msisdn, subscriber in subscribers.items()
    }
    unknown_subscriber_cdrs = []
    suspicious_calls = []
    total_cost = 0.0

    for cdr in cdrs:
        cost = compute_cost(cdr.call_type, cdr.duration_sec)
        total_cost += cost
        suspicious = is_suspicious(cdr.duration_sec)
        summary = subscriber_summaries.get(cdr.msisdn)

        if summary is None:
            unknown_subscriber_cdrs.append({
                "msisdn": cdr.msisdn,
                "call_type": cdr.call_type,
                "duration_sec": cdr.duration_sec,
                "cost": cost,
            })
        else:
            summary["call_count"] += 1
            summary["total_duration_sec"] += cdr.duration_sec
            summary["total_cost"] = round(summary["total_cost"] + cost, 2)
            if suspicious:
                summary["suspicious_call_count"] += 1

        if suspicious:
            suspicious_calls.append({
                "msisdn": cdr.msisdn,
                "call_type": cdr.call_type,
                "duration_sec": cdr.duration_sec,
                "cost": cost,
            })

    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "summary": {
            "subscriber_count": len(subscribers),
            "valid_cdr_count": len(cdrs),
            "rejected_cdr_count": len(rejected_records),
            "billed_amount": round(sum(item["total_cost"] for item in subscriber_summaries.values()), 2),
            "unassigned_amount": round(sum(item["cost"] for item in unknown_subscriber_cdrs), 2),
            "processed_amount": round(total_cost, 2),
            "suspicious_call_count": len(suspicious_calls),
        },
        "subscriber_billing": subscriber_summaries,
        "suspicious_calls": suspicious_calls,
        "unknown_subscriber_cdrs": unknown_subscriber_cdrs,
        "rejected_cdrs": rejected_records,
    }

def write_report(report: dict, output_file: str | Path) -> None:
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)
