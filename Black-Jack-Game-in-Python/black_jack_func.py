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
    while True:
        x = input("Hit or Stand? (h / s)")

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            return False

        else:
            print("Wrong character on input")
            continue
        break
        return True


def show_first(player, dealer):
    print("DEALER'S HAND: \n{}\nCard hidden".format(dealer.cards[0]))
    print("PLAYER'S HAND: \n{}".format(player))


def show_all(player, dealer):
    print("DEALER'S HAND: \n{}".format(dealer))
    print("PLAYER'S HAND: \n{}".format(player))
