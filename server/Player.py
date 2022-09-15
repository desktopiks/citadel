from server.Characters.Character import Character


class Player(object):
    def __init__(self, player_name):
        self.character = Character(None)
        self.player_name = player_name
        self.districts_in_hand = []
        self.districts_in_table = []

    def choose_character(self, character):
        self.character = character

    def get_info(self):
        pass

    def get_progress_information(self):
        return self.character.get_progress_information(self, self.districts_in_table)

    def get_districts_in_hand(self, list_of_districts):
        self.districts_in_hand.extend(list_of_districts)

    def put_cards_on_the_table(self, districts):
        self.districts_in_table.extend(set(districts))
        for district in districts:
            self.districts_in_hand.remove(district)

