from enum import Enum


class Suit(Enum):
    SPADE = ('Spade', False, '♤')
    HEART = ('Heart', True, '♥')
    DIAMOND = ('Diamond', True, '◆')
    Club = ('Club', False, '♧')

    def __init__(self, name: str, colored: bool, suit: str):
        self.name = name
        self.colored = colored
        self.suit = suit


class PlayingCard:
    def __init__(self, suit: Suit, number: int):
        self.suit = suit
        self.number = number

    def __str__(self):
        d = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        number = d[self.number] if self.number in d.keys() else self.number
        return f'{self.suit.suit}{number}'


class FreeCell:
    def __init__(self):
        self.cell = []

    def push(self, element: PlayingCard):
        if len(self.cell) < 4:
            self.cell.append(element)

    def pop(self, index: int):
        if 0 <= index < len(self.cell):
            return self.cell.pop(index)
