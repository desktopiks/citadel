class Character(object):
    """Is a Basic character class"""

    def __init__(self, character_name):
        """Constructor"""
        self.character_name = character_name

    def action(self, self_player, other_player, list_of_the_districts):
        """The action of this character"""
        pass

    @staticmethod
    def get_info(self):
        """Print info of this character"""
        return '''You play for {}
     In your turn, you need to {}
        '''

    @staticmethod
    def get_progress_information(self, districts):
        """Print info of this action"""
        return 'In your turn you {} '

    @staticmethod
    def number_of_districts_can_build():
        return 1

    @staticmethod
    def is_warlord_can_destroy_your_districts():
        return True

    @staticmethod
    def is_thief_can_rob_you():
        return True
