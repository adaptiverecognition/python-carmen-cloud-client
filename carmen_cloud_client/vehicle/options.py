from dataclasses import dataclass
from typing import Optional, Tuple
from enum import Enum

@dataclass
class SelectedServices:
    """
    Specifies the recognition services to call on the input image.
    """
    anpr: Optional[bool] = True
    mmr: Optional[bool] = True
    adr: Optional[bool] = False

@dataclass
class InputImageLocation:
    """
    Represents the geographic location where the input image was taken.
    """
    region: str
    location: Optional[str] = None

@dataclass
class RegionOfInterest:
    """
    Represents the region of interest to be analyzed in the input image.
    The coordinates are given as `(x, y)` pairs.
    """
    topLeft: Tuple[float, float]
    topRight: Tuple[float, float]
    bottomRight: Tuple[float, float]
    bottomLeft: Tuple[float, float]

class Europe:
    Hungary = InputImageLocation(region="EUR", location="HUN")
    Austria = InputImageLocation(region="EUR", location="AUT")
    Slovakia = InputImageLocation(region="EUR", location="SVK")
    Czechia = InputImageLocation(region="EUR", location="CZE")
    Slovenia = InputImageLocation(region="EUR", location="SVN")
    Poland = InputImageLocation(region="EUR", location="POL")
    Estonia = InputImageLocation(region="EUR", location="EST")
    Latvia = InputImageLocation(region="EUR", location="LVA")
    Lithuania = InputImageLocation(region="EUR", location="LTU")
    Romania = InputImageLocation(region="EUR", location="ROU")
    Bulgaria = InputImageLocation(region="EUR", location="BGR")
    Croatia = InputImageLocation(region="EUR", location="HRV")
    BosniaHerzegovina = InputImageLocation(region="EUR", location="BIH")
    Serbia = InputImageLocation(region="EUR", location="SRB")
    NorthMacedonia = InputImageLocation(region="EUR", location="MKD")
    Montenegro = InputImageLocation(region="EUR", location="MNE")
    Albania = InputImageLocation(region="EUR", location="ALB")
    Greece = InputImageLocation(region="EUR", location="GRC")
    Turkey = InputImageLocation(region="EUR", location="TUR")
    Netherlands = InputImageLocation(region="EUR", location="NLD")
    Luxembourg = InputImageLocation(region="EUR", location="LUX")
    Germany = InputImageLocation(region="EUR", location="DEU")
    Belgium = InputImageLocation(region="EUR", location="BEL")
    France = InputImageLocation(region="EUR", location="FRA")
    FranceOverseasTerritories = InputImageLocation(region="EUR", location="FRA_OT")
    Switzerland = InputImageLocation(region="EUR", location="CHE")
    Italy = InputImageLocation(region="EUR", location="ITA")
    Portugal = InputImageLocation(region="EUR", location="PRT")
    Spain = InputImageLocation(region="EUR", location="ESP")
    EuropeanOrganization = InputImageLocation(region="EUR", location="NONE")
    Denmark = InputImageLocation(region="EUR", location="DNK")
    DenmarkFaroe = InputImageLocation(region="EUR", location="FRO")
    DenmarkGreenland = InputImageLocation(region="EUR", location="GRL")
    Norway = InputImageLocation(region="EUR", location="NOR")
    Sweden = InputImageLocation(region="EUR", location="SWE")
    Finland = InputImageLocation(region="EUR", location="FIN")
    FinlandAland = InputImageLocation(region="EUR", location="FIN")
    GreatBritain = InputImageLocation(region="EUR", location="GBR")
    Gibraltar = InputImageLocation(region="EUR", location="GIB")
    IsleOfMan = InputImageLocation(region="EUR", location="IMN")
    Jersey = InputImageLocation(region="EUR", location="JEY")
    Guernsey = InputImageLocation(region="EUR", location="GGY")
    Alderney = InputImageLocation(region="EUR", location="ALD")
    GreatBritainNorthernIreland = InputImageLocation(region="EUR", location="NIR")
    Ireland = InputImageLocation(region="EUR", location="IRL")
    Russia = InputImageLocation(region="EUR", location="RUS")
    Ukraine = InputImageLocation(region="EUR", location="UKR")
    UkraineLuhansk = InputImageLocation(region="EUR", location="UKR")
    UkraineDonetsk = InputImageLocation(region="EUR", location="UKR")
    Moldova = InputImageLocation(region="EUR", location="MDA")
    MoldovaTransnistria = InputImageLocation(region="EUR", location="MDA")
    Belarus = InputImageLocation(region="EUR", location="BLR")
    Georgia = InputImageLocation(region="EUR", location="GEO")
    GeorgiaAbkhazia = InputImageLocation(region="EUR", location="GEO")
    GeorgiaSouthOssetia = InputImageLocation(region="EUR", location="GEO")
    Azerbaijan = InputImageLocation(region="EUR", location="AZE")
    Armenia = InputImageLocation(region="EUR", location="ARM")
    Kazakhstan = InputImageLocation(region="CAS", location="KAZ")
    Andorra = InputImageLocation(region="EUR", location="AND")
    Monaco = InputImageLocation(region="EUR", location="MCO")
    Liechtenstein = InputImageLocation(region="EUR", location="LIE")
    SanMarino = InputImageLocation(region="EUR", location="SMR")
    VaticanCity = InputImageLocation(region="EUR", location="VAT")
    Kosovo = InputImageLocation(region="EUR", location="RKS")
    Iceland = InputImageLocation(region="EUR", location="ISL")
    Malta = InputImageLocation(region="EUR", location="MLT")
    CyprusSouthCyprus = InputImageLocation(region="EUR", location="CYP")
    CyprusUNCyprus = InputImageLocation(region="EUR", location="NONE")
    CyprusNorthCyprus = InputImageLocation(region="EUR", location="CYP")
    SvalbardAndJanMayen = InputImageLocation(region="EUR", location="SJM")

class NorthAmerica:
    UnitedStatesOfAmericaGovernment = InputImageLocation(region="NAM", location="NONE")
    UnitedStatesOfAmericaColumbia = InputImageLocation(region="NAM", location="US-DC")
    UnitedStatesOfAmericaAlaska = InputImageLocation(region="NAM", location="US-AK")
    UnitedStatesOfAmericaWashington = InputImageLocation(region="NAM", location="US-WA")
    UnitedStatesOfAmericaOregon = InputImageLocation(region="NAM", location="US-OR")
    UnitedStatesOfAmericaCalifornia = InputImageLocation(region="NAM", location="US-CA")
    UnitedStatesOfAmericaIdaho = InputImageLocation(region="NAM", location="US-ID")
    UnitedStatesOfAmericaNevada = InputImageLocation(region="NAM", location="US-NV")
    UnitedStatesOfAmericaMontana = InputImageLocation(region="NAM", location="US-MT")
    UnitedStatesOfAmericaWyoming = InputImageLocation(region="NAM", location="US-WY")
    UnitedStatesOfAmericaUtah = InputImageLocation(region="NAM", location="US-UT")
    UnitedStatesOfAmericaArizona = InputImageLocation(region="NAM", location="US-AZ")
    UnitedStatesOfAmericaNorthDakota = InputImageLocation(region="NAM", location="US-ND")
    UnitedStatesOfAmericaSouthDakota = InputImageLocation(region="NAM", location="US-SD")
    UnitedStatesOfAmericaNebraska = InputImageLocation(region="NAM", location="US-NE")
    UnitedStatesOfAmericaColorado = InputImageLocation(region="NAM", location="US-CO")
    UnitedStatesOfAmericaNewMexico = InputImageLocation(region="NAM", location="US-NM")
    UnitedStatesOfAmericaKansas = InputImageLocation(region="NAM", location="US-KS")
    UnitedStatesOfAmericaOklahoma = InputImageLocation(region="NAM", location="US-OK")
    UnitedStatesOfAmericaTexas = InputImageLocation(region="NAM", location="US-TX")
    UnitedStatesOfAmericaArkansas = InputImageLocation(region="NAM", location="US-AR")
    UnitedStatesOfAmericaMinnesota = InputImageLocation(region="NAM", location="US-MN")
    UnitedStatesOfAmericaWisconsin = InputImageLocation(region="NAM", location="US-WI")
    UnitedStatesOfAmericaIowa = InputImageLocation(region="NAM", location="US-IA")
    UnitedStatesOfAmericaIllinois = InputImageLocation(region="NAM", location="US-IL")
    UnitedStatesOfAmericaMissouri = InputImageLocation(region="NAM", location="US-MO")
    UnitedStatesOfAmericaMichigan = InputImageLocation(region="NAM", location="US-MI")
    UnitedStatesOfAmericaIndiana = InputImageLocation(region="NAM", location="US-IN")
    UnitedStatesOfAmericaOhio = InputImageLocation(region="NAM", location="US-OH")
    UnitedStatesOfAmericaKentucky = InputImageLocation(region="NAM", location="US-KY")
    UnitedStatesOfAmericaAlabama = InputImageLocation(region="NAM", location="US-AL")
    UnitedStatesOfAmericaTennessee = InputImageLocation(region="NAM", location="US-TN")
    UnitedStatesOfAmericaLouisiana = InputImageLocation(region="NAM", location="US-LA")
    UnitedStatesOfAmericaMississippi = InputImageLocation(region="NAM", location="US-MS")
    UnitedStatesOfAmericaMaine = InputImageLocation(region="NAM", location="US-ME")
    UnitedStatesOfAmericaVermont = InputImageLocation(region="NAM", location="US-VT")
    UnitedStatesOfAmericaNewHampshire = InputImageLocation(region="NAM", location="US-NH")
    UnitedStatesOfAmericaConnecticut = InputImageLocation(region="NAM", location="US-CT")
    UnitedStatesOfAmericaMassachusetts = InputImageLocation(region="NAM", location="US-MA")
    UnitedStatesOfAmericaRhodeIsland = InputImageLocation(region="NAM", location="US-RI")
    UnitedStatesOfAmericaNewYork = InputImageLocation(region="NAM", location="US-NY")
    UnitedStatesOfAmericaNewJersey = InputImageLocation(region="NAM", location="US-NJ")
    UnitedStatesOfAmericaDelaware = InputImageLocation(region="NAM", location="US-DE")
    UnitedStatesOfAmericaPennsylvania = InputImageLocation(region="NAM", location="US-PA")
    UnitedStatesOfAmericaMaryland = InputImageLocation(region="NAM", location="US-MD")
    UnitedStatesOfAmericaVirginia = InputImageLocation(region="NAM", location="US-VA")
    UnitedStatesOfAmericaWestVirginia = InputImageLocation(region="NAM", location="US-WV")
    UnitedStatesOfAmericaNorthCarolina = InputImageLocation(region="NAM", location="US-NC")
    UnitedStatesOfAmericaSouthCarolina = InputImageLocation(region="NAM", location="US-SC")
    UnitedStatesOfAmericaGeorgia = InputImageLocation(region="NAM", location="US-GA")
    UnitedStatesOfAmericaFlorida = InputImageLocation(region="NAM", location="US-FL")
    UnitedStatesOfAmericaHawaii = InputImageLocation(region="NAM", location="US-HI")
    UnitedStatesOfAmericaPuertoRico = InputImageLocation(region="NAM", location="US-PR")
    UnitedStatesOfAmericaGuam = InputImageLocation(region="NAM", location="US-GU")
    UnitedStatesOfAmericaAmericanSamoa = InputImageLocation(region="NAM", location="US-AS")
    UnitedStatesOfAmericaVirginIslands = InputImageLocation(region="NAM", location="US-VI")
    UnitedStatesOfAmericaNorthernMarianaIslands = InputImageLocation(region="NAM", location="US-MP")
    CanadaFederal = InputImageLocation(region="NAM", location="NONE")
    CanadaBritishColumbia = InputImageLocation(region="NAM", location="CA-BC")
    CanadaAlberta = InputImageLocation(region="NAM", location="CA-AB")
    CanadaSaskatchewan = InputImageLocation(region="NAM", location="CA-SK")
    CanadaManitoba = InputImageLocation(region="NAM", location="CA-MB")
    CanadaOntario = InputImageLocation(region="NAM", location="CA-ON")
    CanadaQuebec = InputImageLocation(region="NAM", location="CA-QC")
    CanadaNovaScotia = InputImageLocation(region="NAM", location="CA-NS")
    CanadaNewBrunswick = InputImageLocation(region="NAM", location="CA-NB")
    CanadaNewfoundlandLabrador = InputImageLocation(region="NAM", location="CA-NL")
    CanadaNorthWestTerritories = InputImageLocation(region="NAM", location="CA-NT")
    CanadaNunavut = InputImageLocation(region="NAM", location="CA-NU")
    CanadaPrinceEdouardIsland = InputImageLocation(region="NAM", location="CA-PE")
    CanadaYukon = InputImageLocation(region="NAM", location="CA-YT")

class CentralAmerica:
    Guatemala = InputImageLocation(region="CAM", location="GTM")
    Belize = InputImageLocation(region="CAM", location="BLZ")
    ElSalvador = InputImageLocation(region="CAM", location="SLV")
    Nicaragua = InputImageLocation(region="CAM", location="NIC")
    Honduras = InputImageLocation(region="CAM", location="HND")
    CostaRica = InputImageLocation(region="CAM", location="CRI")
    Panama = InputImageLocation(region="CAM", location="PAN")
    Mexico = InputImageLocation(region="CAM", location="MEX")

class SouthAmerica:
    Colombia = InputImageLocation(region="SAM", location="COL")
    Venezuela = InputImageLocation(region="SAM", location="VEN")
    Guyana = InputImageLocation(region="SAM", location="GUY")
    Suriname = InputImageLocation(region="SAM", location="SUR")
    Peru = InputImageLocation(region="SAM", location="PER")
    Brazil = InputImageLocation(region="SAM", location="BRA")
    Ecuador = InputImageLocation(region="SAM", location="ECU")
    Bolivia = InputImageLocation(region="SAM", location="BOL")
    Paraguay = InputImageLocation(region="SAM", location="PRY")
    Chile = InputImageLocation(region="SAM", location="CHL")
    Argentina = InputImageLocation(region="SAM", location="ARG")
    Uruguay = InputImageLocation(region="SAM", location="URY")
    FalklandIslands = InputImageLocation(region="SAM", location="FLK")

class CentralAsia:
    Uzbekistan = InputImageLocation(region="CAS", location="UZB")
    Turkmenistan = InputImageLocation(region="CAS", location="TKM")
    Tajikistan = InputImageLocation(region="CAS", location="TJK")
    Kyrgyzstan = InputImageLocation(region="CAS", location="KGZ")
    Mongolia = InputImageLocation(region="CAS", location="MNG")
    Afghanistan = InputImageLocation(region="CAS", location="AFG")

class EastAsia:
    China = InputImageLocation(region="EAS", location="CHN")
    HongKong = InputImageLocation(region="EAS", location="HKG")
    Macau = InputImageLocation(region="EAS", location="MAC")
    KoreaSouth = InputImageLocation(region="EAS", location="KOR")
    KoreaNorth = InputImageLocation(region="EAS", location="PRK")

class SouthAsia:
    Thailand = InputImageLocation(region="SAS", location="THA")
    Malaysia = InputImageLocation(region="SAS", location="MYS")
    Singapore = InputImageLocation(region="SAS", location="SGP")
    Myanmar = InputImageLocation(region="SAS", location="MMR")
    Laos = InputImageLocation(region="SAS", location="LAO")
    Cambodia = InputImageLocation(region="SAS", location="KHM")
    Vietnam = InputImageLocation(region="SAS", location="VNM")
    Brunei = InputImageLocation(region="SAS", location="BRN")
    ChristmasIsland = InputImageLocation(region="SAS", location="CXR")
    KeelingIslands = InputImageLocation(region="SAS", location="CCK")

class MiddleEast:
    Syria = InputImageLocation(region="ARAB", location="SYR")
    Lebanon = InputImageLocation(region="ARAB", location="LBN")
    Jordan = InputImageLocation(region="ARAB", location="JOR")
    SaudiArabia = InputImageLocation(region="ARAB", location="SAU")
    Kuwait = InputImageLocation(region="ARAB", location="KWT")
    UnitedArabEmirates = InputImageLocation(region="ARAB", location="ARE")
    Qatar = InputImageLocation(region="ARAB", location="QAT")
    Bahrain = InputImageLocation(region="ARAB", location="BHR")
    Oman = InputImageLocation(region="ARAB", location="OMN")
    Yemen = InputImageLocation(region="ARAB", location="YEM")

class AustraliaAndOceania:
    AustraliaUnknown = InputImageLocation(region="AUS", location="NONE")
    AustraliaFederalInterstate = InputImageLocation(region="AUS", location="NONE")
    AustraliaGovernment = InputImageLocation(region="AUS", location="NONE")
    AustraliaCapitalTerritory = InputImageLocation(region="AUS", location="AU-ACT")
    AustraliaNorthernTerritory = InputImageLocation(region="AUS", location="AU-NT")
    AustraliaNewSouthWales = InputImageLocation(region="AUS", location="AU-NSW")
    AustraliaQueensland = InputImageLocation(region="AUS", location="AU-QLD")
    AustraliaSouthAustralia = InputImageLocation(region="AUS", location="AU-SA")
    AustraliaTasmania = InputImageLocation(region="AUS", location="AU-TAS")
    AustraliaVictoria = InputImageLocation(region="AUS", location="AU-VIC")
    AustraliaWesternAustralia = InputImageLocation(region="AUS", location="AU-WA")

class Locations:
    """
    An object which contains all accepted region/location pairs.
    """
    Europe = Europe
    NorthAmerica = NorthAmerica
    CentralAmerica = CentralAmerica
    SouthAmerica = SouthAmerica
    CentralAsia = CentralAsia
    EastAsia = EastAsia
    SouthAsia = SouthAsia
    MiddleEast = MiddleEast
    AustraliaAndOceania = AustraliaAndOceania
