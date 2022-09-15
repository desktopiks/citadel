from CharactersList import CharactersList
from server.Characters.Character import Character
from server.District import DistrictTypeList


class Bishop(Character):

    def __init__(self):
        super().__init__(CharactersList.Bishop)
        self.text = "You receive one gold for each religious (blue) district in your city."

    def action(self, character_name=None):
        """The action of this character"""

    def get_progress_information(self, districts_in_hand):
        """Print info of this action"""
        return super(Bishop, self).get_progress_information(self).format("You receive {} gold").format(len(list(filter(lambda x: x.value.type_of_district == DistrictTypeList.Religious, districts_in_hand))))

    def get_info(self):
        """Print info of this character"""
        return super(Bishop, self).get_info(self).format(self.character_name, self.text)
