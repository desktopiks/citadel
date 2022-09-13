from backend.Characters.Character import Character


class Player(object):

    def __init__(self, player_name):
        self.character = Character(None)
        self.player_name = player_name

    def choose_character(self, character):
        self.character = character

    def get_info(self):
        pass

    def get_progress_information(self):

        pass
