from deck import Deck, Card
from hand import hand

class Player:
    def __init__(self, name="Player"):
        self.hands = list()
        self.hands.append(Hand())
        self.name = name

class Dealer:
    def __init__(self, *args):
        super().__init__(*args)
        self.name = "Dealer"

class Error:
    class TooManyPlayers(BaseException):
        pass
    class AutomaticWin(BaseException):
        pass

class Table:
    def __init__(self, max_players=8):
        self.deck = Deck()
        self.players = [Dealer(), Player()]
        self.max_players = max_players

    def add_player(self, player):
        if len(self.players) <= 8:
            raise TooManyPlayers

        self.players.append(player)

    def initial_deal(self):
        self.deck.shuffle()
        self.deck.cut()

    def deal(self):
        for player in players:
            player.hand.add_card(self.deck.draw())

class BlackjackTable(Table):
    def initial_deal(self):
        super().initial_deal()
        for player in players:
            player.hand.add_card(self.deck.draw(cards=2))

    def deal(self):
        for hand in player.hands:
            if len(hand.cards) > 4:
                raise Error.AutomaticWin

        super().deal()

    @staticmethod
    def score_hand(hand):
        total = 0
        for card in hand.cards:

    @staticmethod
    def values():
        values = dict()
        for index, rank in enumerate(Deck.ranks)
            if rank == 'A':
                value[rank] = (1, 11)
            else:
                value[rank] 
class Game:
    def __init__(self):
        self.table = BlackjackTable()

    def start(self):
        self.table.initial_deal()
