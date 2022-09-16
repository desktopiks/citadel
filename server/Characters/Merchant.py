from CharactersList import CharactersList
from server.Characters.Character import Character
from server.District import DistrictTypeList


class Merchant(Character):

    def __init__(self):
        super().__init__(CharactersList.Assassin)

    def action(self, self_player, other_player):
        """The action of this character"""
        self_player.change_gold(self.get_gold(self_player.districts_in_table))

    def get_progress_information(self, districts_in_table):
        """Print info of this action"""
        return super().get_progress_information(self).format("You receive {} gold").format(self.get_gold(districts_in_table))

    def get_info(self):
        """Print info of this character"""
        return super().get_info(self).format(self.character_name, "You receive one gold for each trade (green)district in your city")

    def get_gold(self, districts_in_table):
        return len(list(filter(lambda x: x.value.type_of_district == DistrictTypeList.Trade, districts_in_table)))