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

    def action(self, character_name):
        """The action of this character"""
        pass

    def get_progress_information(self, districts_in_hand):
        """Print info of this action"""
        return super(King, self).get_progress_information(self).format("You receive {} gold").format(
            len(list(filter(lambda x: x.value.type_of_district == DistrictTypeList.Noble, districts_in_hand))))

    def get_info(self):
        """Print info of this character"""
        return super(King, self).get_info(self).format(self.character_name, self.text)


print(King().get_progress_information(DistrictsList.take_the_cards(4)))
