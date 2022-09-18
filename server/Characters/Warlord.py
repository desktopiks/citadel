from CharactersList import CharactersList
from server.Characters.Character import Character
from server.District import DistrictTypeList, DistrictsList


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
        self.gold = 0

    def action(self, self_player, other_player, district):
        """The action of this character"""
        self.gold = len(list(filter(lambda x: x.value.type_of_district == DistrictTypeList.Religious, self_player.districts_in_table)))
        self_player.change_gold(self.gold)
        other_player.districts_in_table.remove(district)

    def get_progress_information(self):
        """Print info of this action"""
        return super().get_progress_information(self).format("You receive {} gold {}").format(self.gold)

    def get_info(self):
        """Print info of this character"""
        return super().get_info(self).format(self.character_name, self.text)


    @staticmethod
    def can_destroy_district(self_player, other_player, district):
        return other_player.character != CharactersList.Bishop and self_player.gold >= district.price + 1
