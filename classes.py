import random
import cribbage


class Player():
    def __init__(self, one_card, turn="No", dealer="No", said_go="No", score=0):
        self.one_card = one_card
        self.score = score
        self.dealer = dealer
        self.turn = turn
        self.said_go = said_go
        self.hand = []
        self.crib = []
        self.played = []

    def alt_deal(self):
        if self.dealer == "No":
            self.dealer = "Yes"
        elif self.dealer == "Yes":
            self.dealer = "No"

    def alt_turn(self):
        if self.turn == "No":
            self.turn = "Yes"
        elif self.turn == "Yes":
            self.turn = "No"

    def check_score(self):
        print "Your score is: ", self.score
        print "Your opponent's score is: ", opponent.score
        self.display_options()

    def cut_a_card(self):
        self.one_card = random.choice(game.deck)
        return self.one_card

    def discard_to_crib(self):
        print "Choose which cards to pass to the crib"
        for card in self.hand:
            print str(self.hand.index(card) + 1) + ")", card
        print "select a card by typing its corresponding number and press enter"
        discard = raw_input(">>>")
        if int(discard) <= len(self.hand):
            if self.dealer == "Yes":
                self.crib.append(self.hand.pop(int(discard) - 1))
            if opponent.dealer == "Yes":
                opponent.crib.append(self.hand.pop(int(discard) - 1))
        else:
            print "Sorry, that wasn't an option."
        if len(self.crib) == 2:
            print "You threw in: "
            for card in self.crib:
                print card
        elif len(opponent.crib) == 2:
            print "You threw in: "
            for card in opponent.crib:
                print card

    def display_options(self):
        print """Here are your options:
        """
        print "[P]lay a Card"
        print "Say [G]o"
        # print "[O]rganize Hand"
        print "Check [S]core"
        print "Review [C]ards Played"
        # print "[Q]uit Game"
        action = str(raw_input(">>>"))
        if action == "P" or action == "p":
            self.play_card()
        elif action == "G" or action == "g":
            self.say_go()
        # elif action == "O" or action == "o":
        #     organize_hand()
        elif action == "S" or action == "s":
            self.check_score()
        elif action == "C" or action == "c":
            self.review_cards_played()
        # elif action == "Q" or action == "q":
        #     game.end_game()
        else:
            print "Sorry, that wasn't an option."
            self.display_options()

    def end_turn(self):
        self.alt_turn()
        opponent.alt_turn()
        opponent.take_turn()

    def move_peg(self, points):
        self.score += points
        if self.score > 120:
            print "You Won!"

    def play_card(self):
        print "select a card by typing its corresponding number and press enter"
        print "or [R]eturn to options"
        for card in self.hand:
            print str(self.hand.index(card) + 1) + ")", card
        play = raw_input(">>>")
        if play == "R" or play == "r":
            self.display_options()
        else:
            try:
                if int(play) <= len(self.hand):
                    tried = []
                    tried.append(self.hand.pop(int(play) - 1))
                    if tried[0].value <= (31 - cycle.tot):
                        self.played.append(tried.pop())
                        cycle.lcp = self.played[-1]
                        print "You played:", cycle.lcp
                        cycle.new_tot(cycle.lcp.value)
                        cycle.append_lcp_list()
                        cycle.peg()
                        self.end_turn()
                    else:
                        print "That card is too big to play!"
                        self.hand.append(tried.pop())
                        self.play_card()
                else:
                    print "Sorry, that wasn't an option."
                    self.play_card()
            except ValueError:
                print "Sorry, that wasn't an option."
                self.play_card()

    def review_cards_played(self):
        print cycle.lcp
        self.display_options()

    def say_go(self):
        self.said_go = "Yes"
        self.end_turn()

    def take_turn(self):
        if len(self.hand) > 0:
            print "Your hand is: "
            for card in self.hand:
                print card
        self.display_options()


class Bot():
    def __init__(self, one_card, turn="No", dealer="No", said_go="No", score=0):
        self.one_card = one_card
        self.score = score
        self.dealer = dealer
        self.turn = turn
        self.said_go = said_go
        self.hand = []
        self.crib = []
        self.played = []

    def alt_deal(self):
        if self.dealer == "No":
            self.dealer = "Yes"
        elif self.dealer == "Yes":
            self.dealer = "No"

    def alt_turn(self):
        if self.turn == "No":
            self.turn = "Yes"
        elif self.turn == "Yes":
            self.turn = "No"

    def cut_a_card(self):
        self.one_card = random.choice(game.deck)
        return self.one_card

    def discard_to_crib(self):
        if self.dealer == "Yes":
            self.crib.append(self.hand.pop())
        if player.dealer == "Yes":
            player.crib.append(self.hand.pop())

    def end_turn(self):
        self.alt_turn()
        player.alt_turn()
        player.take_turn()

    def move_peg(self, points):
        self.score += points
        if self.score > 120:
            print "Your opponent won :("

    def take_turn(self):
        self.played.append(self.hand.pop())
        cycle.lcp = self.played[-1]
        print "Your opponent played: ", cycle.lcp
        cycle.new_tot(cycle.lcp.value)
        cycle.append_lcp_list()
        self.end_turn()


class Game():
    def __init__(self, players, bots, status):
        self.players = players
        self.bots = bots
        self.status = status
        self.deck = cribbage.cards

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def compare_cut(self):
        print "You showed " + str(player.one_card) + " and your opponent showed " + str(opponent.one_card) + "."
        test = cribbage.Card.__cmp__(player.one_card, opponent.one_card)
        if test == 1:
            print "You will take the first deal."
            player.alt_deal()
            opponent.alt_turn()
        else:
            print "Your opponent will take the first deal."
            opponent.alt_deal()
            player.alt_turn()
        self.deal_hand()

    def deal_hand(self):
        # self.shuffle_deck()
        while len(player.hand) < 6:
            player.hand.append(self.deck.pop())
        while len(opponent.hand) < 6:
            opponent.hand.append(self.deck.pop())
        print player.hand


class Cycle():
    def __init__(self, rid=0, fuc=None, lcp=None, tot=0):
        self.rid = rid
        self.lcp = lcp
        self.lcp_list = []
        self.fuc = fuc
        self.tot = tot

    def append_lcp_list(self):
        self.lcp_list.append(self.lcp)

    def clear_lcp_list(self):
        self.lcp_list = []

    def next_round(self):
        self.rid += 1

    def new_lcp(self):
        self.lcp = []

    def new_fuc(self):
        if player.dealer == "Yes":
            player.cut_a_card()
            self.fuc = player.one_card
            print "The common card is: ", str(self.fuc)
            if "Jack" in str(self.fuc):
                player.move_peg(2)
                print "2 points for you!"
        elif opponent.dealer == "Yes":
            opponent.cut_a_card()
            self.fuc = opponent.one_card
            print "The common card is: ", str(self.fuc)
            if "Jack" in str(self.fuc):
                opponent.move_peg(2)
                print "2 points for your opponent :("

    def new_tot(self, value):
        self.tot += value

        if self.tot == 15:
            if player.turn == "Yes":
                print "15 for 2 points for you!"
                player.move_peg(2)
            if opponent.turn == "Yes":
                print "15 for 2 points for your opponent :("
                opponent.move_peg(2)
        elif self.tot == 31:
            if player.turn == "Yes":
                print "31 for 2 points for you!"
                player.move_peg(2)
            if opponent.turn == "Yes":
                print "31 for 2 points for your opponent :("
                opponent.move_peg(2)
            self.tot = 0
        print "The count is: ", self.tot

    def peg(self):
        try:
            if self.lcp_list[-1].rank == self.lcp_list[-2].rank == self.lcp_list[-3].rank == self.lcp_list[-4].rank:
                print "All 4!: 12 points!"
                if player.turn == "Yes":
                    player.move_peg(12)
                else:
                    opponent.move_peg(12)
            elif self.lcp_list[-1].rank == self.lcp_list[-2].rank == self.lcp_list[-3].rank:
                print "3 of a kind: 6 points!"
                if player.turn == "Yes":
                    player.move_peg(6)
                else:
                    opponent.move_peg(6)
            elif self.lcp_list[-1].rank == self.lcp_list[-2].rank:
                print "Paired up: 2 points!"
                if player.turn == "Yes":
                    player.move_peg(2)
                else:
                    opponent.move_peg(2)
            if self.lcp_list[-1].rank == self.lcp_list[-2].rank + 1 == self.lcp_list[-3].rank + 2 or \
                    self.lcp_list[-1].rank == self.lcp_list[-2].rank - 1 == self.lcp_list[-3].rank - 2 or \
                    self.lcp_list[-1].rank == self.lcp_list[-2].rank + 2 == self.lcp_list[-3].rank + 1 or \
                    self.lcp_list[-1].rank == self.lcp_list[-2].rank - 2 == self.lcp_list[-3].rank - 1:
                print "That's 3 in a row: 3 points!"
                if player.turn == "Yes":
                    player.move_peg(3)
                else:
                    opponent.move_peg(3)
        except IndexError:
            player.end_turn()


game = Game(players=1, bots=1, status=None)
player = Player(one_card=None, turn="No", dealer="No", score=0)
opponent = Bot(one_card=None, turn="No", dealer="No", score=0)
cycle = Cycle(rid=0, fuc=None, lcp=None, tot=0)