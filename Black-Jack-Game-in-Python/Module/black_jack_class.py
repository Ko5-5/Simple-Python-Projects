import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values ={'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
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
        print(" {} , {} ".format(self.rank, self.suit))


class Deck:
    """
    Class that manages the collection of the deck, having function for drawing a card from the deck
    """
    deck = []

    def __init__(self, num_decks=1):
        self.number = (num_decks * 52) - 1
        c = 0
        for i in ranks:
            for j in suits:
                self.deck[c] = Card(i, j)

    def __str__(self):
        for i in range(0, self.number+1):
            print(self.deck[i])

    def draw(self):
        num = random.randint(0, self.number)
        self.number = self.number - 1
        temp = self.deck[num]
        self.deck.pop(num)
        return temp

    def shuffle_deck(self):
        random.shuffle(self.deck)

