import random
from enum import Enum


class DistrictTypeList(Enum):
    Bonus = 0
    Military = 1
    Religious = 2
    Noble = 3
    Trade = 4


class District(object):
    """Is a Basic character class"""

    def __init__(self, name, type_of_district, price, quantity):
        """Constructor"""
        self.name = name
        self.type_of_district = type_of_district
        self.price = price
        self.quantity = quantity


class DistrictsList(Enum):
    Watchtower = District("watchtower", DistrictTypeList.Military, 1, 3)
    Prison = District("prison", DistrictTypeList.Military, 2, 3)
    The_Field_of_Mars = District("the Field of Mars", DistrictTypeList.Military, 3, 3)
    Fortress = District("fortress", DistrictTypeList.Military, 5, 2)

    Temple = District("temple", DistrictTypeList.Religious, 1, 3)
    Church = District("church", DistrictTypeList.Religious, 2, 3)
    Monastery = District("monastery", DistrictTypeList.Religious, 3, 3)
    Cathedral = District("cathedral", DistrictTypeList.Religious, 5, 2)

    Estate = District("estate", DistrictTypeList.Noble, 3, 5)
    Castle = District("castle", DistrictTypeList.Noble, 4, 4)
    Palazzo = District("castle", DistrictTypeList.Noble, 5, 3)

    Tavern = District("tavern", DistrictTypeList.Trade, 1, 5)
    Market = District("market", DistrictTypeList.Trade, 2, 4)
    Shop = District("shop", DistrictTypeList.Trade, 2, 3)
    Port = District("port", DistrictTypeList.Trade, 3, 3)
    Harbor = District("harbor", DistrictTypeList.Trade, 4, 3)
    Guildhall = District("guildhall", DistrictTypeList.Trade, 5, 2)

    @staticmethod
    def take_the_cards(number=1, type_of_district=None):
        return random.choices([i for i in DistrictsList if (type_of_district is None or i.value.type_of_district == type_of_district)], k=number)

