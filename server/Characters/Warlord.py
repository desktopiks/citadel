from CharactersList import CharactersList
from server.Characters.Character import Character
from server.District import DistrictTypeList


class Warlord(Character):

    def __init__(self):
        super().__init__(CharactersList.Warlord)
        self.choose_character = None
        self.text = """You receive one gold for each military (red) 
district in your city. At the end of your turn, you
may destroy one district of your choice by paying 
a number of gold equal to one less than the cost 
of the district. Thus, you may destroy a cost one
district for free, a cost two district for one gold,
or a cost six district for five gold, etc. You may
destroy one of your own districts. You may not, 
however, destroy a district in a city that is already 
completed by having eight districts (or seven 
districts when the Bell Tower is in play)."""

    def action(self, character_name):
        """The action of this character"""
        self.choose_character = character_name

    def get_progress_information(self, districts_in_hand):
        """Print info of this action"""
        return super(Warlord, self).get_progress_information(self).format("You receive {} gold").format(len(list(filter(lambda x: x.value.type_of_district == DistrictTypeList.Religious, districts_in_hand))))

    def get_info(self):
        """Print info of this character"""
        return super(Warlord, self).get_info(self).format(self.character_name, self.text)

