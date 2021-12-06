from enum import Enum


class Suit(Enum):
    SPADE = ('Spade', False)
    HEART = ('Heart', True)
    DIAMOND = ('Diamond', True)
    Club = ('Club', False)

    def __init__(self, name: str, colored: bool):
        self.name = name
        self.colored = colored
