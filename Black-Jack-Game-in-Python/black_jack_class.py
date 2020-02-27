import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    """
    A class that surves the purpose of creating an card
    """

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    """
    Class that manages the collection of the deck, having function for drawing a card from the deck
    """

    def __init__(self):
        self.deck = []
        for k in ranks:
            for j in suits:
                self.deck.append(Card(k, j))

    def __str__(self):
        deck_comp = ''
        for car in self.deck:
            deck_comp += '\n' + car.__str__()
        return 'The deck : ' + deck_comp

    def draw(self):
        num = random.randint(0, len(self.deck) - 1)
        loc = self.deck[num]
        self.deck.pop(num)
        return loc

    def shuffle_deck(self):
        random.shuffle(self.deck)


class Hand:
    """
    Class created to store the hand of a player or dealer
    """

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        hand_comp = ''
        for car in self.cards:
            hand_comp += car.__str__() + '\n'
        return hand_comp

    def add_card(self, car):
        self.cards.append(car)
        self.value += car.value

        if car.rank == "Ace":
            self.aces += 1

    def adjust_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    """
    Class created to store the balance of a player
    """

    def __init__(self, cash=1000):
        self.total = cash
        self.bet = 0

    def bet_win(self):
        self.total += int(self.bet * 1.5)

    def bet_lose(self):
        self.total -= self.bet
