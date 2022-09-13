class Character(object):
    """Is a Basic character class"""

    def __init__(self, character_name):
        """Constructor"""
        self.choose_character = None
        self.character_name = character_name

    def action(self, character_name):
        """The action of this character"""
        self.choose_character = character_name
        pass

    def get_info(self):
        """Print info of this character"""
        pass

    def get_progress_information(self):
        """Print info of this action"""
        pass

