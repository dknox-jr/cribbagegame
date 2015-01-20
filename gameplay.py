import random
import cribbage
import classes


def start_game():
    print "Cut to see who will deal first."
    cut_for_deal()


def shuffle_deck():
    random.shuffle(cribbage.cards)
    return cribbage.cards


def cut_for_deal():
    shuffle_deck()
    player_card = cribbage.cards.pop()
    computer_card = cribbage.cards.pop()
    print "You showed " + str(player_card) + " and your opponent showed " + str(computer_card) + "."
    compare_cut(player_card, computer_card)
    return player_card, computer_card


def compare_cut(player_card, computer_card):
    test = cribbage.Card.__cmp__(player_card, computer_card)
    if test == 1:
        print "You will take the first deal."
        classes.current_player.altturn()
        deal_hand()
    else:
        print "Your opponent will take the first deal."
        classes.opponent.altturn()
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
    face_up(myhand, opphand)
    return myhand, opphand


def face_up(myhand, opphand):
    up_card = cribbage.cards.pop()
    print "The Common card is: ", up_card
    play_hand(myhand, opphand)
    return up_card


def play_hand(myhand, opphand):
    if classes.current_player.turn == True:
        display_options(myhand, opphand)
    elif classes.opponent.turn == True:
        opponent_turn(myhand, opphand)
    return myhand, opphand


def display_options(myhand, opphand):
    print """Here are your options:
        """
    if len(myhand) > 0:
        print "[P]lay a card"
        print "say [G]o"
        print "[O]rganize hand"
    action = raw_input(">>>")
    if action == "P" or "p":
        play_card(myhand, opphand)
    elif action == "G" or "g":
        say_go()
    elif action == "O" or "o":
        organize_hand()
    else:
        print "Sorry, that wasn't an option."
        display_options(myhand, opphand)


def play_card(myhand, opphand):
    for card in myhand:
        print str(myhand.index(card) + 1) + ")", card
    print "select a card by typing its corresponding number and press enter"
    play = raw_input(">>>")
    if int(play) <= len(myhand):
        my_played = myhand.pop(int(play) - 1)
        print "You played ", my_played
        end_player_turn(myhand, opphand)
        return myhand, my_played
    else:
        print "Sorry, that wasn't an option."
        play_card(myhand, opphand)


def opponent_turn(myhand, opphand):
    opp_play = opphand.pop()
    print "Your opponent played: ", opp_play
    end_opponent_turn(myhand, opphand)
    return opp_play, opphand


def end_player_turn(myhand, opphand):
    classes.current_player.altturn()
    classes.opponent.altturn()
    opponent_turn(myhand, opphand)


def end_opponent_turn(myhand, opphand):
    classes.opponent.altturn()
    classes.current_player.altturn()
    play_card(myhand, opphand)

start_game()
