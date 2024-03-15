from enum import Enum


class SanjnaPrakaara(Enum):
    """संज्ञाप्रकाराः"""

    UPADESHA = "उपदेश"
    DHAATU = "धातु"
    GUNA = "गुण"
    VRIDDHI = "वृद्धि"
    PRATYAYA = "प्रत्यय"
    KRIT = "कृत्"
    IT = "इत्"


class SvaraBheda(Enum):
    """स्वरभेदः"""

    UDATTA = "उदात्त"
    ANUDATTA = "अनुदात्त"
    SVARITA = "स्वरित"


class Gana(Enum):
    """गणः"""

    BHVADI = "१"
    ADADI = "२"
    JUHOTYADI = "३"
    DIVADI = "४"
    SVADI = "५"
    TUDADI = "६"
    RUDHADI = "७"
    TANADI = "८"
    KRYADI = "९"
    CHURADI = "१०"
