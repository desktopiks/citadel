from CharactersList import CharactersList
from server.Characters.Character import Character
from server.District import DistrictTypeList, DistrictsList


class King(Character):

    def __init__(self):
        super().__init__(CharactersList.King)
        self.text = """You receive one gold for each noble (yellow)
district in your city.
When the King is called, you immediately receive
the Crown. You now call the characters, and you
will be the first player to choose your character
during the next round."""

    def action(self, self_player, other_player, list_of_the_districts):
        """The action of this character"""
        self_player.change_gold(self.get_gold(self_player.districts_in_table))

    def get_progress_information(self, districts_in_table):
        """Print info of this action"""
        return super(King, self).get_progress_information(self).format("You receive {} gold").format(self.get_gold(districts_in_table))

    def get_info(self):
        """Print info of this character"""
        return super().get_info(self).format(self.character_name, self.text)

    @staticmethod
    def get_gold(districts_in_table):
        len(list(filter(lambda x: x.value.type_of_district == DistrictTypeList.Noble, districts_in_table)))


# print(King().get_progress_information(DistrictsList.take_the_cards(4)))
