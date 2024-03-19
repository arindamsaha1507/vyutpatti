"""कार्यस्य वर्तमानस्थितिः"""

from dataclasses import dataclass, field

from akshara import varnakaarya as vk
from dhaatu import Dhaatu
from globs import SanjnaPrakaara


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

    def __repr__(self) -> str:
        return f"[[{self.start_index}, {self.end_index}], {self.sanjna}]"


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
    
    def __repr__(self) -> str:
        return f"{self.kramaanka}"


@dataclass
class Sthiti:
    """वर्तमानस्थितिः"""

    sopaana: Sopaana
    sthiti: str
    sanjna: list[Sanjna]
    sutra: str
    purva_sopaana: Sopaana
    contents: list = field(default_factory=list)
    vyaakhyaa: str = field(default="")

    @property
    def vinyaasa(self):
        """विन्यासः"""
        return vk.get_vinyaasa(self.sthiti)

    @property
    def length(self):
        """परिमाणम्"""
        return len(self.vinyaasa)
    
    def __repr__(self) -> str:
        return f"| {self.sopaana} | {self.sthiti} | {self.sutra} | {self.vyaakhyaa} |"


class SthitiFactory:
    """वर्तमानस्थितिः निर्माणकर्ता"""

    @staticmethod
    def initiate(dhaatu_pankti: Sopaana):
        """वर्तमानस्थितिः आरभते"""

        contents = dhaatu_pankti.split(" ")

        if len(contents) < 3:
            raise ValueError("अतिलघ्वी धातुपङ्क्तिः")

        kramaanka = contents[0]
        dhaatu = contents[1]
        artha = " ".join(contents[2:])

        dh = Dhaatu(kramaanka=kramaanka, upadesha=dhaatu, artha=artha)

        return Sthiti(
            sopaana=Sopaana([0]),
            sthiti=dh.upadesha,
            sanjna=[
                Sanjna(0, len(vk.get_vinyaasa(dh.upadesha)), SanjnaPrakaara.UPADESHA)
            ],
            sutra="-",
            purva_sopaana=None,
            contents = [dh],
            vyaakhyaa=f"धातुपाठे पठितः धातुः {dh.upadesha} {dh.artha} । अतः उपदेशसञ्ज्ञकः ॥",
        )


def main():
    """Main Function"""

    dhaatu_pankti = "८.१० डुकृ॒ञ् कर॑णे"
    sthiti = SthitiFactory.initiate(dhaatu_pankti)
    print(sthiti)


if __name__ == "__main__":
    main()
