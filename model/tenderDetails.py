from dataclasses import dataclass
from typing import Dict, List, Literal, Optional

@dataclass
class LocationSchema:
    orszag: str
    iranyitoszam: str
    telepules: str
    kozterNeve: str
    kozterJellege: str
    hazszam: str
    helyrajziszam: str
    nutsKod: str


@dataclass
class PurchaserSchema:
    id: int
    rovidMegnevezes: int
    teljesMegnevezes: str
    szekhely: LocationSchema
    ajanlatkeroJogalapok20200722Utan: str
    kozszolgaltatoJogalap: str
    fotevekenysegiKod: str


@dataclass
class TenderDetailsSchema:
    vezetoAjanlatkeroSzervezet: PurchaserSchema
    kozbeszerzesiEljaras: Dict[str, str]
    kapcsolodoDokumentumok: List[Dict[str, str]]
    erdeklodesJelzeseEljarasra: bool
    erdeklodesJelzeseOsszefoglaloTajekoztatoAlapajan: bool
    elozetesenErdeklodesJelzeseEljarasra: bool
    hirdetmenyek: List[Dict[str, str]]

    def __post_init__(self):
        self.purchaser = PurchaserSchema(**self.vezetoAjanlatkeroSzervezet)