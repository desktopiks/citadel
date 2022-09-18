from CharactersList import CharactersList
from server.Characters.Character import Character
from server.District import DistrictsList


class Architect(Character):

    def __init__(self):
        super().__init__(CharactersList.Architect)
        self.new_cards = None
        self.text = "After you take an action, you draw two additional district cards and put both in your hand."

    def action(self, self_player, other_player, list_of_the_districts):
        self.new_cards = DistrictsList.take_the_cards(2)
        self_player.districts_in_hand.extend(self.new_cards)
        """The action of this character"""

    def get_progress_information(self):
        """Print info of this action"""
        return super().get_progress_information(self).format("You receive {} {}").format(", ".join([self.new_cards[i].name for i in range(len(self.new_cards) - 1)]) if self.new_cards else "0", str(self.new_cards[len(self.new_cards) - 1].name) if self.new_cards else "cards")

    def get_info(self):
        """Print info of this character"""
        return super().get_info(self).format(self.character_name, self.text)

    def number_of_districts_can_build(self):
        return 3

