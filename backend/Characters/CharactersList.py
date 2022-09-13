from enum import Enum


class CharactersList(Enum):
    Null = 0
    Assassin = 10
    Witch = 11
    Thief = 20
    TaxCollector = 21
    Magician = 30
    Wizard = 31
    King = 40
    Emperor = 41
    Bishop = 50
    Abbot = 51
    Merchant = 60
    Alchemist = 61
    Architect = 70
    Navigator = 71
    Warlord = 80
    Diplomat = 81
    Artist = 91
    Queen = 92

    @staticmethod
    def all_characters():
        return [i for i in CharactersList]

    @staticmethod
    def default_characters():
        return [i for i in CharactersList if i.value % 10]
