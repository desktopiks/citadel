class Character(object):
    """Is a Basic character class"""

    def __init__(self, character_name):
        """Constructor"""
        self.character_name = character_name

    def action(self, character_name):
        """The action of this character"""
        pass

    @staticmethod
    def get_info(self):
        """Print info of this character"""
        return '''You play for {}
     In your turn, you need to {}
        '''

    @staticmethod
    def get_progress_information(self):
        """Print info of this action"""
        return 'In your turn you {} '



