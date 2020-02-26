import random
import time

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


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Your bet: "))
        except:
            print("Please provide a number")
        else:
            if chips.bet > chips.total:
                print("The value exceeds your chips balance, you only have: {}".format(chips.total))
            else:
                break


def hit(deck, hand):
    single_card = deck.draw()
    hand.add_card(single_card)
    hand.adjust_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Hit or Stand? (h / s)")

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False

        else:
            print("Wrong character on input")
            continue
        break


def show_first(player, dealer):
    print("DEALER'S HAND: \n{}\nCard hidden".format(dealer.cards[0]))
    print("PLAYER'S HAND: \n{}".format(player))


def show_all(player, dealer):
    print("DEALER'S HAND: \n{}".format(dealer))
    print("PLAYER'S HAND: \n{}".format(player))


if __name__ == '__main__':
    game_on = True
    chips = Chips()
    win = int
    print("Welcome to a game of BLACK JACK")

    while game_on:
        print("Creating a new deck...")
        deck = Deck()
        print("Shuffling the deck...")
        deck.shuffle_deck()
        print("Available player chips: {}".format(chips.total))
        take_bet(chips)

        dealer = Hand()
        player = Hand()

        dealer.add_card(deck.draw())
        dealer.add_card(deck.draw())
        player.add_card(deck.draw())
        player.add_card(deck.draw())

        playing = True

        while playing and player.value <= 21:
            show_first(player, dealer)
            print("Player Hand Value: {}".format(player.value))
            hit_or_stand(deck, player)

        if player.value > 21:
            win = 0
            print("BUST!")
        else:
            show_all(player, dealer)

            print("Dealer: {}".format(dealer.value))
            print("Player: {}".format(player.value))

            time.sleep(3)

            while dealer.value < 17:
                dealer.add_card(deck.draw())

                show_all(player, dealer)

                print("Dealer: {}".format(dealer.value))
                print("Player: {}".format(player.value))

        if (dealer.value > 21 >= player.value) or (dealer.value < player.value <= 21) or ():
            print("Player wins, here are your chips")
            chips.bet_win()
            print("Added {} chips to your previous balance".format(int(chips.bet * 0.5)))
        elif win == 0 or player.value < dealer.value <= 21:
            print("Player loses, your bet is lost")
            chips.bet_lose()
            print("Lost {} chips".format(chips.bet))
        elif dealer.value == player.value:
            print("oh, it's a draw, your bet is returned")

        print("Available player chips: {}".format(chips.total))

        if chips.total < 1:
            print("You've lost all your chips")
            break

        temp = input("Would you like to play again?(y/n): ")
        if temp == 'y':
            game_on = True
        else:
            game_on = False

    print("Thanks for playing!")
