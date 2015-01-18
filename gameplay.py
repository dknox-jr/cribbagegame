import random
import cribbage
import classes


def start_game():
    print "Cut to see who will deal first."
    cut_for_deal()


def shuffle_deck():
    random.shuffle(cribbage.cards)


def cut_for_deal():
    random.shuffle(cribbage.cards)
    player_card = cribbage.cards.pop()
    computer_card = cribbage.cards.pop()
    print "You showed " + str(player_card) + " and your opponent showed " + str(computer_card) + "."
    compare_cut(player_card, computer_card)
    return player_card, computer_card


def compare_cut(player_card, computer_card):
    test = cribbage.Card.__cmp__(player_card, computer_card)
    if test == 1:
        print "You will take the first deal."
        classes.current_player.dealer = True
        deal_hand()
    else:
        print "Your opponent will take the first deal."
        classes.opponent.dealer = True
        deal_hand()


def deal_hand():
    shuffle_deck()
    myhand = classes.current_player.hand
    opphand = classes.opponent.hand

    while len(myhand) < 6:
        myhand.append(cribbage.cards.pop())
    while len(opphand) < 6:
        opphand.append(cribbage.cards.pop())

    print "Your hand is: "
    for card in myhand:
        print card
    display_options(myhand)
    return myhand, opphand


def display_options(myhand):
    print """Here are your options:
    """
    if len(myhand) > 0:
        print "[P]lay a card"
        print "say [G]o"
        print "[O]rganize hand"
    action = raw_input(">>>")
    if action == "P" or "p":
        for card in myhand:
            print card



start_game()
