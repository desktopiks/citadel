from CharactersList import CharactersList
from server.Characters.Character import Character


class Assassin(Character):

    def __init__(self):
        super().__init__(CharactersList.Assassin)
        self.choose_character = None
        self.text = "Choose any character and kill him"

    def action(self, self_player, other_player, list_of_the_districts):
        """The action of this character"""
        self.choose_character = other_player.character
        other_player.character = None

    def get_progress_information(self, districts_in_hand=None):
        """Print info of this action"""
        return super(Assassin, self).get_progress_information(self, None).format("kill {}").format(self.choose_character)

    def get_info(self):
        """Print info of this character"""
        return super(Assassin, self).get_info(self).format(self.character_name, "choose any character and kill him")

    def is_thief_can_rob_you(self):
        return False
