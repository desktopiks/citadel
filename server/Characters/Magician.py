from CharactersList import CharactersList
from server.Characters.Character import Character


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
        self.choose_move = True

    def action(self, choose_move):
        """The action of this character"""
        self.choose_move = choose_move

    def get_progress_information(self):
        """Print info of this action"""
        return super(Magician, self).get_progress_information(self).format(self.first_move if self.choose_move else self.second_move)

    def get_info(self):
        """Print info of this character"""
        return super(Magician, self).get_info(self).format(self.character_name, """{} \n Or \n {}""").format(
            self.first_move, self.second_move)


t1 = Magician()
t1.action(CharactersList.King)
print(t1.get_info())
print(t1.get_progress_information())
