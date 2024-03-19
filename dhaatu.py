"""धातूनां वर्णनात्मकः सङ्घः"""

from dataclasses import dataclass, field

import akshara.varnakaarya as vk

from globs import Gana, SvaraBheda


@dataclass
class Dhaatu:
    """धातुः"""

    kramaanka: str
    upadesha: str
    artha: str
    gana: Gana = field(init=False, repr=False)
    dhaatu: str = field(init=False, repr=False)
    it_svara: SvaraBheda = field(init=False, default=SvaraBheda.UDATTA)
    svara: SvaraBheda = field(init=False, default=SvaraBheda.UDATTA)

    def __post_init__(self):

        if len(self.kramaanka.split(".")) != 2:
            raise ValueError("kramaanka should be of the form 'x.y'")

        self.remove_swara_markings()

    def remove_swara_markings(self) -> str:
        """Remove swara markings from the upadesha."""

        upa = []

        for idx, char in enumerate(self.upadesha):
            if char not in ("॒", "॑"):
                upa.append(char)
            else:
                if char == "॒":
                    if self.upadesha[idx - 1] == "ँ":
                        self.it_svara = SvaraBheda.ANUDATTA
                    else:
                        self.svara = SvaraBheda.ANUDATTA
                else:
                    if self.upadesha[idx - 1] == "ँ":
                        self.it_svara = SvaraBheda.SVARITA
                    else:
                        self.svara = SvaraBheda.SVARITA

        self.upadesha = "".join(upa)


if __name__ == "__main__":
    dhaatu = Dhaatu(
        kramaanka="८.१०",
        upadesha="डुकृ॒ञ्",
        artha="कर॑णे",
    )
    print(dhaatu)
    print(dhaatu.upadesha)
    print(vk.get_vinyaasa(dhaatu.upadesha))
