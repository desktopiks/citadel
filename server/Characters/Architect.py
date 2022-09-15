from CharactersList import CharactersList
from server.Characters.Character import Character


class Architect(Character):

    def __init__(self):
        super().__init__(CharactersList.Architect)
        self.choose_character = None

    def action(self, character_name):
        """The action of this character"""
        self.choose_character = character_name

    def get_progress_information(self):
        """Print info of this action"""
        return super(Architect, self).get_progress_information(self).format("You receive {} gold").format()

    def get_info(self):
        """Print info of this character"""
        return super(Architect, self).get_info(self).format(self.character_name, "After you take an action, you draw two additional district cards and put both in your hand.")

