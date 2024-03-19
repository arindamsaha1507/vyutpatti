"""वैय्याकरणप्रक्रिया"""

from dataclasses import dataclass, field

from sthiti import Sthiti

@dataclass
class Prakriyaa:
    """प्रक्रिया"""

    prakriyaa: list[Sthiti] = field(default=None)

    def get_sopaana(self):
        """सोपानानि प्राप्नोति"""

        if self.prakriyaa is None:
            return []

        return [sthiti.sopaana for sthiti in self.prakriyaa]

    def add_sthiti(self, sthiti: Sthiti):
        """वर्तमानस्थितिः योजयति"""

        if self.prakriyaa is None:
            self.prakriyaa = []

        if sthiti.purva_sopaana is None:
            pass
        else:
            if sthiti.purva_sopaana not in self.get_sopaana():
                raise ValueError("पूर्वसोपानः अस्मिन् प्रक्रियायां नास्ति")

        self.prakriyaa.append(sthiti)
