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
        for i in ranks:
            for j in suits:
                self.deck.append(Card(i, j))

    def __str__(self):
        deck_comp = ''
        for car in self.deck:
            deck_comp += '\n' + car.__str__()
        return 'The deck : ' + deck_comp

    def draw(self):
        num = random.randint(0, len(self.deck) - 1)
        temp = self.deck[num]
        self.deck.pop(num)
        return temp

    def shuffle_deck(self):
        random.shuffle(self.deck)


if __name__ == '__main__':
    game_on = True
    chips = 1000
    win = int
    print("Welcome to a game of BLACK JACK")
    while game_on:
        print("Creating a new deck...")
        deck = Deck()
        print("Shuffling the deck...")
        deck.shuffle_deck()
        print("Available player chips: {}".format(chips))
        bet = 0
        check = True
        while check:
            bet = int(input("Player's bet: "))
            if bet > chips:
                print("Your bet exceeds available founds")
                check = True
            else:
                check = False
        chips = chips - bet

        dealer = []
        player = []

        dealer.append(deck.draw())
        dealer.append(deck.draw())
        player.append(deck.draw())
        player.append(deck.draw())

        print("\n")
        print("Dealer's cards: ")
        print(dealer[0])
        print("Hidden card\n")
        print("Player's cards: ")
        for card in player:
            print(card)
        print("\n")

        summary_dealer = 0
        summary_player = 0

        for i in dealer:
            summary_dealer += i.value
        for i in player:
            summary_player += i.value

        ans = input("Hit - (y/n): ")

        while ans == 'y' and summary_player <= 21:
            player.append(deck.draw())
            print("\n")
            print("Dealer's cards: ")
            print(dealer[0])
            print("Hidden card\n")
            print("\nPlayer's cards: ")
            for card in player:
                print(card)
            print("\n")

            summary_player = 0
            for i in player:
                summary_player += i.value
            if summary_player > 21:
                break

            ans = input("Hit - (y/n): ")

        if summary_player > 21:
            win = 0
            print("BUST!")
        else:
            print("\n")
            print("Dealer's cards: ")
            for card in dealer:
                print(card)
            print("\nPlayer's cards: ")
            for card in player:
                print(card)
            print("\n")

            summary_dealer = 0

            for i in dealer:
                summary_dealer += i.value

            print("Dealer: {}".format(summary_dealer))
            print("Player: {}".format(summary_player))

            while summary_dealer < 17:
                dealer.append(deck.draw())
                print("\n")
                print("Dealer's cards: ")
                for card in dealer:
                    print(card)
                print("\nPlayer's cards: ")
                for card in player:
                    print(card)
                print("\n")

                summary_dealer = 0

                for i in dealer:
                    summary_dealer += i.value

                print("Dealer: {}".format(summary_dealer))
                print("Player: {}".format(summary_player))

        if (summary_dealer > 21 >= summary_player) or (summary_dealer < summary_player <= 21) or ():
            print("Player wins, here are your chips")
            chips += int(bet*1.5)
            print("Added {} chips to your previous balance".format(int(bet*0.5)))
        elif win == 0 or summary_player < summary_dealer <= 21:
            print("Player loses, your bet is lost")
            print("Lost {} chips".format(bet))
        elif summary_dealer == summary_player:
            print("oh, it's a draw, your bet is returned")
            chips += bet

        print("Available player chips: {}".format(chips))

        if chips < 1:
            print("You've lost all your chips")
            break

        temp = input("Would you like to play again?(y/n): ")
        if temp == 'y':
            game_on = True
        else:
            game_on = False

    print("Thanks for playing!")
