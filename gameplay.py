import random
import cribbage


def start_game():
    print "Cut to see who will deal first."
    cut_for_deal()


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
    else:
        print "Your opponent will take the first deal."


start_game()