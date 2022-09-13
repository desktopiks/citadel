import Character
from CharactersList import CharactersList


class Assassin(Character):

    def __init__(self):
        super().__init__(self, CharactersList.Assassin)

    def action(self, character_name):
        """The action of this character"""
        super(Assassin, self).action(self, character_name)

    def get_progress_information(self):
        text_character = super(Assassin, self).get_progress_information(self)
        """Print info of this action"""
        pass
