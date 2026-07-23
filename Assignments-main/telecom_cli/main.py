from datetime import date
import logging
from pathlib import Path

from config import LOG_FILE
from io_utils import load_cdrs_with_errors, load_subscribers
from reporting import build_report, write_report


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
REPORT_PATH = BASE_DIR / "reports" / "telecom_billing_report.json"
LOG_PATH = BASE_DIR / "logs" / LOG_FILE


def configure_logging() -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=LOG_PATH,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        force=True,
    )

def main() -> None:
    configure_logging()
    print("=" * 50)
    print("Telecom CDR & Billing Insights CLI")
    print(f"Date: {date.today()}")
    print("=" * 50)

    try:
        subscribers = load_subscribers(DATA_DIR / "subscribers.json")
        cdrs, rejected_records = load_cdrs_with_errors(DATA_DIR / "cdrs.csv")
        report = build_report(subscribers, cdrs, rejected_records)
        write_report(report, REPORT_PATH)
    except (OSError, ValueError, KeyError) as error:
        logging.exception("Report generation failed: %s", error)
        raise

    logging.info(
        "Report generated: valid_cdrs=%d rejected_cdrs=%d billed_amount=%.2f suspicious_calls=%d",
        report["summary"]["valid_cdr_count"],
        report["summary"]["rejected_cdr_count"],
        report["summary"]["billed_amount"],
        report["summary"]["suspicious_call_count"],
    )
    for error in rejected_records:
        logging.warning("Rejected CDR: %s", error)
    for cdr in report["unknown_subscriber_cdrs"]:
        logging.warning("Unknown subscriber CDR: %s", cdr["msisdn"])
    for cdr in report["suspicious_calls"]:
        logging.warning("Suspicious CDR: %s", cdr["msisdn"])

    print(f"Report written to: {REPORT_PATH}")
    print(f"Processed CDRs: {report['summary']['valid_cdr_count']}")
    print(f"Billed amount: {report['summary']['billed_amount']:.2f}")
    print(f"Suspicious calls: {report['summary']['suspicious_call_count']}")

if __name__ == "__main__":
    main() 
