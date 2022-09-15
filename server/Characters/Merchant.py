from CharactersList import CharactersList
from server.Characters.Character import Character
from server.District import DistrictTypeList


class Merchant(Character):

    def __init__(self):
        super().__init__(CharactersList.Assassin)

    def action(self, character_name=None):
        """The action of this character"""

    def get_progress_information(self, districts_in_hand):
        """Print info of this action"""
        return super(Merchant, self).get_progress_information(self).format("You receive {} gold").format(len(list(filter(lambda x: x.value.type_of_district == DistrictTypeList.Trade, districts_in_hand))))

    def get_info(self):
        """Print info of this character"""
        return super(Merchant, self).get_info(self).format(self.character_name, "You receive one gold for each trade (green)district in your city")
