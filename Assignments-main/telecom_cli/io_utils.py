import csv
import json
from typing import Dict

from models import Subscriber, CDR


def parse_cdr_line(row: Dict) -> Dict:

    try:
        return {
            "msisdn": row["msisdn"].strip(),
            "call_type": row["call_type"].strip().lower(),
            "duration_sec": int(row["duration_sec"])
        }

    except KeyError as e:
        raise ValueError(f"Missing field: {e}")

    except ValueError:
        raise ValueError("Invalid duration_sec")


def load_subscribers(filepath: str) -> dict[str, Subscriber]:

    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    subscribers = {}

    for item in data:
        subscriber = Subscriber(
            msisdn=item["msisdn"],
            plan_type=item["plan_type"]
        )

        subscribers[subscriber.msisdn] = subscriber

    return subscribers


def load_cdrs(filepath: str) -> list[CDR]:

    cdrs, errors = load_cdrs_with_errors(filepath)
    if errors:
        raise ValueError(errors[0])
    return cdrs


def load_cdrs_with_errors(filepath: str) -> tuple[list[CDR], list[str]]:
    """Load valid CDRs and retain row-level validation errors for reporting."""

    cdrs = []
    errors = []

    with open(filepath, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=2):
            try:
                cleaned_row = parse_cdr_line(row)
            except ValueError as error:
                errors.append(f"Row {row_number}: {error}")
                continue

            cdr = CDR(
                msisdn=cleaned_row["msisdn"],
                call_type=cleaned_row["call_type"],
                duration_sec=cleaned_row["duration_sec"]
            )

            cdrs.append(cdr)

    return cdrs, errors
