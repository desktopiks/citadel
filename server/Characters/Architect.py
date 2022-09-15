from CharactersList import CharactersList
from server.Characters.Character import Character
from server.District import DistrictsList


class Architect(Character):

    def __init__(self):
        super().__init__(CharactersList.Architect)
        self.choose_character = None
        self.text = "After you take an action, you draw two additional district cards and put both in your hand."

    def action(self, character_name):
        """The action of this character"""
        self.choose_character = character_name

    def get_progress_information(self, list_of_cards):
        """Print info of this action"""
        return super(Architect, self).get_progress_information(self).format("You receive {} {}").format(
            ", ".join([list_of_cards[i].name for i in range(len(list_of_cards) - 1)]),
            str(list_of_cards[len(list_of_cards) - 1].name))

    def get_info(self):
        """Print info of this character"""
        return super(Architect, self).get_info(self).format(self.character_name, self.text)


# print(Architect().get_progress_information(DistrictsList.take_the_cards(3)))
