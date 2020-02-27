import time
import black_jack_class as cl
import black_jack_func as fu

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

if __name__ == '__main__':
    game_on = True
    chips = cl.Chips()
    win = int
    print("Welcome to a game of BLACK JACK")

    while game_on:
        print("Creating a new deck...")
        deck = cl.Deck()
        print("Shuffling the deck...")
        deck.shuffle_deck()
        print("Available player chips: {}".format(chips.total))
        fu.take_bet(chips)

        dealer = cl.Hand()
        player = cl.Hand()

        dealer.add_card(deck.draw())
        dealer.add_card(deck.draw())
        player.add_card(deck.draw())
        player.add_card(deck.draw())

        playing = True

        while playing and player.value <= 21:
            fu.show_first(player, dealer)
            print("Player Hand Value: {}".format(player.value))
            playing = fu.hit_or_stand(deck, player)

        if player.value > 21:
            win = 0
            fu.show_all(player, dealer)
            print("Dealer: {}".format(dealer.value))
            print("Player: {}".format(player.value))
            print("BUST!")
        else:
            fu.show_all(player, dealer)
            print("Dealer: {}".format(dealer.value))
            print("Player: {}".format(player.value))

            while dealer.value < 17:
                dealer.add_card(deck.draw())
                fu.show_all(player, dealer)
                print("Dealer: {}".format(dealer.value))
                print("Player: {}".format(player.value))
                time.sleep(1)

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
