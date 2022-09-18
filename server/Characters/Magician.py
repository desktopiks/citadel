from CharactersList import CharactersList
from server.Characters.Character import Character
from server.District import DistrictsList


class Magician(Character):

    def __init__(self):
        super().__init__(CharactersList.Magician)
        self.first_move = """ Exchange your entire hand of cards (not the
        cards in your city) with the hand of another player
        (this applies even if you have no cards in your
        hand, in which case you simply take the other
        player’s cards)."""
        self.second_move = """ Place any number of cards from your hand
        facedown at the bottom of the District Deck, and
        then draw an equal number of cards from the top
        of the District Deck."""
        self.list_of_the_card = None

    def action(self, self_player, other_player, list_of_the_districts):
        """The action of this character"""
        self.list_of_the_card = list_of_the_districts
        if other_player:
            other_player.districts_in_hand, self_player.districts_in_hand = self_player.districts_in_hand, other_player.districts_in_hand
        else:
            for i in self.list_of_the_card:
                self_player.districts_in_hand.remove(i)
            self.list_of_the_card = DistrictsList.take_the_cards(len(self.list_of_the_card))
            self_player.districts_in_hand.extend(self.list_of_the_card)

    def get_progress_information(self, districts=None):
        """Print info of this action"""
        return super().get_progress_information(self, None).format("Your change {} cards").format(len(self.list_of_the_card))

    def get_info(self):
        """Print info of this character"""
        return super().get_info(self).format(self.character_name, """{} \n Or \n {}""").format(self.first_move, self.second_move)

A = Magician()
print(A.get_progress_information())