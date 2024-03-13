"""कार्यस्य वर्तमानस्थितिः"""

from dataclasses import dataclass
from enum import Enum
from akshara import varnakaarya as vk


class SanjnaPrakaara(Enum):
    """संज्ञाप्रकाराः"""

    DHAATU = "धातु"
    GUNA = "गुण"
    VRIDDHI = "वृद्धि"
    PRATYAYA = "प्रत्यय"
    KRIT = "कृत्"
    IT = "इत्"


@dataclass
class Sanjna:
    """संज्ञा"""

    start_index: int
    end_index: int
    sanjna: SanjnaPrakaara

    def __post_init__(self):
        if self.start_index < 0:
            raise ValueError("start_index should be greater than or equal to 0")
        if self.end_index < 0:
            raise ValueError("end_index should be greater than or equal to 0")
        if self.start_index > self.end_index:
            raise ValueError("start_index should be less than or equal to end_index")


@dataclass
class Sopaana:
    """सोपानः"""

    idx: list[int]

    @property
    def kramaanka(self) -> str:
        """क्रमाङ्कः"""
        return ".".join(map(str, self.idx))

    @property
    def shaakhaa(self) -> int:
        """शाखा"""
        return len(self.idx) - 1


@dataclass
class Sthiti:
    """वर्तमानस्थितिः"""

    sopaana: Sopaana
    sthiti: str
    sanjna: list[Sanjna]
    purva_sopaana: Sopaana

    @property
    def vinyaasa(self):
        """विन्यासः"""
        return vk.get_vinyaasa(self.sthiti)

    @property
    def length(self):
        """परिमाणम्"""
        return len(self.vinyaasa)
