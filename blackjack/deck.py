import random
from pprint import pprint

SUITS = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', \
        '10', 'J', 'Q', 'K', 'A']

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        return f"Deck contains {self.cards}"

    def shuffle(self):
        random.shuffle(self.cards)

    def cut(self):
        half = len(self.cards) // 2
        self.cards = self.cards[half:half*2] + self.cards[:half]

    def draw(self, cards=1):
        return [self.cards.pop(0) for _ in range(cards)]

if __name__ == '__main__':
    deck = Deck()

    # pprint(deck.cards)
    deck.shuffle()
    pprint(deck.cards)
    print('-----------------')
    deck.cut()
    pprint(deck.cards)
