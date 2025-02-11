from dataclasses import dataclass
from typing import Dict, List, Literal, Optional


@dataclass
class PurchaserSchema:
    id: int
    sid: int
    name: str


@dataclass
class AwardedSchema:
    date: str
    value_for_two: float
    value_for_two_eur: float
    suppliers: List[Dict[str, str]]
    value_for_three: float
    value_for_one_eur: float
    count: int
    value_for_one: float
    value_for_three_eur: float
    suppliers_id: int
    value_eur: float
    offers_count: List[int]
    suppliers_name: str
    value: float
    offers_count_date: Dict[str, str]


@dataclass
class TenderSchema:
    id: str
    date: str
    deadline_date: str
    title: str
    category: str
    phase: str
    phase_en: str
    sid: str
    eid: str
    awarded_value: str
    awarded_currency: str
    awarded_value_eur: str
    purchaser: PurchaserSchema
    type: Dict[str, str]
    awarded: List[AwardedSchema]
    deadline_length_days: Optional[str] = None
    indicators: List[str] = None
    description: Optional[str] = None
    place: Optional[str] = None


@dataclass
class ApiResponse:
    page_count: int
    page_number: int
    page_size: int
    total: int
    data: List[TenderSchema]

    def __post_init__(self):
        self.data = [TenderSchema(**x) for x in self.data]


@dataclass
class ApiParameters:
    page: Optional[str] = None

