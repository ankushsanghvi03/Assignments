from dataclasses import dataclass

@dataclass
class Subscriber:
    msisdn: str
    plan_type: str

@dataclass
class CDR:
    msisdn: str
    call_type: str
    duration_sec: int