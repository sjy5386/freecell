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


class Foundation:
    def __init__(self):
        self.piles = {
            Suit.SPADE: [],
            Suit.HEART: [],
            Suit.DIAMOND: [],
            Suit.Club: []
        }

    def push(self, element: PlayingCard):
        pile = self.piles[element.suit]
        if (len(pile) > 0 and pile[-1] == element.number - 1) or element.number == 1:
            pile.append(element)


class LineStack:
    def __init__(self):
        self.stack = []

    def push(self, element: PlayingCard):
        if len(self.stack) == 0 or (
                self.stack[-1].number == element.number + 1 and self.stack[-1].suit.colored != element.suit.colored):
            self.stack.append(element)

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()

    def __str__(self):
        return self.stack.__str__()


class FreeCell:
    def __init__(self):
        self.cell = []

    def push(self, element: PlayingCard):
        if len(self.cell) < 4:
            self.cell.append(element)

    def pop(self, index: int):
        if 0 <= index < len(self.cell):
            return self.cell.pop(index)


class FreeCellGame:
    def __init__(self):
        self.foundation = Foundation()
        self.line_stacks = [LineStack() for i in range(8)]
        self.free_cell = FreeCell()
