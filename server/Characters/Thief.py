from CharactersList import CharactersList
from server.Characters.Character import Character


class Thief(Character):

    def __init__(self):
        super().__init__(CharactersList.Thief)
        self.choose_character = None
        self.text = "choose any character and rob him"

    def action(self, self_player, other_player, list_of_the_districts):
        """The action of this character"""
        self.choose_character = other_player.character
        self_player.change_gold(other_player.gold)
        other_player.change_gold(-other_player.gold)

    def get_progress_information(self):
        """Print info of this action"""
        return super().get_progress_information(self).format("rob {}").format(self.choose_character)

    def get_info(self):
        """Print info of this character"""
        return super().get_info(self).format(self.character_name, self.text)

    def can_rab(self, other_character):
        return other_character != CharactersList.Assassin

