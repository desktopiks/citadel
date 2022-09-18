from server.Characters.Character import Character
from server.Characters.CharactersList import CharactersList
from server.District import DistrictsList


class Player(object):
    def __init__(self, player_name):
        self.character = Character(None)
        self.player_name = player_name
        self.districts_in_hand = DistrictsList.take_the_cards(4)
        self.districts_in_table = set()
        self.gold = 2

    def choose_character(self, character):
        self.character = character

    def get_info(self):
        pass

    def get_progress_information(self):
        return self.character.get_progress_information(self.character, self.districts_in_table) if self.character else ""

    def get_districts_in_hand(self, list_of_districts):
        self.districts_in_hand.extend(list_of_districts) if self.character else ""

    def put_cards_on_the_table(self, districts):
        for district in districts:
            if district not in self.districts_in_table:
                self.districts_in_hand.remove(district)
                self.districts_in_table.add(district)
                self.change_gold(district.price)

    def character_move(self, other_player, district):
        if self.character == CharactersList.Assassin:
            self.character.action(self, other_player, None)
        elif self.character == CharactersList.Thief:
            self.character.action(self, other_player, None)
        elif self.character == CharactersList.Magician:
            self.character.action(self, other_player, [])
        elif self.character == CharactersList.King:
            self.character.action(self, None, None)
        elif self.character == CharactersList.Bishop:
            self.character.action(self, None, None)
        elif self.character == CharactersList.Merchant:
            self.character.action(self, None, None)
        elif self.character == CharactersList.Architect:
            self.character.action(self, None, None)
        elif self.character == CharactersList.Warlord:
            self.character.action(self, other_player, district)

    def second_move(self, change_move):
        if change_move == 1:
            self.change_gold(2)
            return None
        elif change_move == 2:
            return DistrictsList.take_the_cards(2)

    def after_move(self):
        if self.character == CharactersList.Architect:
            self.get_districts_in_hand(DistrictsList.take_the_cards(2))
        elif self.character == CharactersList.Merchant:
            self.change_gold(1)

    def second_move_path_two(self, district):
        self.get_districts_in_hand([district])

    def return_districts(self):
        return self.districts_in_table, self.districts_in_hand

    def change_gold(self, number):
        self.gold += number

    def number_of_districts_can_build(self):
        return self.character.number_of_districts_can_build()
