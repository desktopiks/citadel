from server.Characters.Character import Character


class Player(object):
    def __init__(self, player_name):
        self.character = Character(None)
        self.player_name = player_name
        self.districts_in_hand = []
        self.districts_in_table = set()
        self.gold = 0

    def choose_character(self, character):
        self.character = character

    def get_info(self):
        pass

    def get_progress_information(self):
        return self.character.get_progress_information(self) if self.character else ""

    def get_districts_in_hand(self, list_of_districts):
        self.districts_in_hand.extend(list_of_districts) if self.character else ""

    def put_cards_on_the_table(self, districts):
        for district in districts:
            self.districts_in_hand.remove(district)
            self.districts_in_table.add(district)

    def move(self):
        if self.character ==

    def change_gold(self, number):
        self.gold += number
