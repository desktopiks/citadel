import random
from enum import Enum
from random import randrange


class CharactersList(Enum):
    Assassin = 1
    Witch = 2
    Thief = 3
    TaxCollector = 4
    Magician = 5
    Wizard = 6
    King = 7
    Emperor = 8
    Bishop = 9
    Abbot = 10
    Merchant = 11
    Alchemist = 12
    Architect = 13
    Navigator = 14
    Warlord = 15
    Diplomat = 16
    Artist = 17
    Queen = 18

    @staticmethod
    def all_characters(number):
        return random.choices([i for i in CharactersList], k=number)

    @staticmethod
    def default_characters(number):
        return random.choices([i for i in CharactersList if i.value % 2 == 1 and i.value < 16], k=number)

