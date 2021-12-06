import random
from enum import Enum


class Suit(Enum):
    SPADE = ('♤', False)
    HEART = ('♥', True)
    DIAMOND = ('◆', True)
    Club = ('♧', False)

    def __init__(self, suit: str, colored: bool):
        self.suit = suit
        self.colored = colored


class PlayingCard:
    def __init__(self, suit: Suit, number: int):
        self.suit = suit
        self.number = number

    def __str__(self):
        d = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        number = d[self.number] if self.number in d.keys() else self.number
        return f'{self.suit.suit}{number}'

    def __repr__(self):
        return self.__str__()


class Foundation:
    def __init__(self, fill: bool = False):
        self.piles = {}
        for name, member in Suit.__members__.items():
            self.piles[member] = []

        if fill:
            self.fill()

    def push(self, element: PlayingCard):
        pile = self.piles[element.suit]
        if (len(pile) > 0 and pile[-1].number == element.number - 1) or element.number == 1:
            pile.append(element)

    def fill(self):
        for name, member in Suit.__members__.items():
            for i in range(1, 14):
                self.push(PlayingCard(member, i))

    def empty(self):
        for k, v in self.piles.items():
            v.clear()

    def __str__(self):
        return list(map(lambda e: e[-1] if len(e) > 0 else None,
                        [self.piles[member] for name, member in Suit.__members__.items()])).__str__()


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

    def __str__(self):
        return self.cell.__str__()


class FreeCellGame:
    def __init__(self):
        self.foundation = Foundation(fill=True)
        self.line_stacks = [LineStack() for i in range(8)]
        self.free_cell = FreeCell()

        for i in range(6):
            for j in range(len(self.line_stacks)):
                self.line_stacks[j].stack.append(self.foundation.piles[random.choice(list(Suit))].pop())
        for i in range(len(self.line_stacks) // 2):
            self.line_stacks[i].stack.append(self.foundation.piles[random.choice(list(Suit))].pop())

    def __str__(self):
        return f'Foundations: {self.foundation}\nFree Cells: {self.free_cell}\n' + '\n'.join(
            x.__str__() for x in self.line_stacks)
