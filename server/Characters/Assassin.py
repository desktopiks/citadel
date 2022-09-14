from CharactersList import CharactersList
from server.Characters.Character import Character


class Assassin(Character):

    def __init__(self):
        super().__init__(CharactersList.Assassin)
        self.choose_character = None

    def action(self, character_name):
        """The action of this character"""
        self.choose_character = character_name

    def get_progress_information(self):
        """Print info of this action"""
        return super(Assassin, self).get_progress_information(self).format("kill {}").format(self.choose_character)

    def get_info(self):
        """Print info of this character"""
        return super(Assassin, self).get_info(self).format(self.character_name, "choose any character and kill him")

