from CharactersList import CharactersList
from server.Characters.Character import Character


class Merchant(Character):

    def __init__(self):
        super().__init__(CharactersList.Assassin)

    def action(self, character_name=None):
        """The action of this character"""

    def get_progress_information(self):
        """Print info of this action"""
        return super(Merchant, self).get_progress_information(self).format("You receive {} gold").format()

    def get_info(self):
        """Print info of this character"""
        return super(Merchant, self).get_info(self).format(self.character_name, "You receive one gold for each trade (green)district in your city")
