class Player():
    def __init__(self, turn="No", dealer="No", score=0):
        self.score = score
        self.dealer = dealer
        self.turn = turn
        self.hand = []
        self.crib = []

    def altturn(self):
        if self.turn == "No":
            self.turn = "Yes"
        elif self.turn == "Yes":
            self.turn = "No"

    def altdeal(self):
        if self.dealer == "No":
            self.dealer = "Yes"
        elif self.dealer == "Yes":
            self.dealer = "No"

    def move_peg(self):
        if self.score > 120:
            print "You Won!"
        else:
            self.score += 1

current_player = Player(turn="No", dealer="No", score=0)


class Bot():
    def __init__(self, turn="No", dealer="No", score=0):
        self.score = score
        self.dealer = dealer
        self.turn = turn
        self.hand = []
        self.crib = []

    def altturn(self):
        if self.turn == "No":
            self.turn = "Yes"
        elif self.turn == "Yes":
            self.turn = "No"

    def altdeal(self):
        if self.dealer == "No":
            self.dealer = "Yes"
        elif self.dealer == "Yes":
            self.dealer = "No"

    def move_peg(self):
        self.score += 1

opponent = Bot(turn="No", dealer="No", score=0)


class Round():
    def __init__(self, rid=0, fuc=None, lcp=None, tot=0):
        self.rid = rid
        self.lcp = lcp
        self.fuc = fuc
        self.tot = tot

    def next_round(self):
        self.rid += 1

    def new_lcp(self):
        self.lcp = []

    def new_fuc(self):
        self.fuc = []
        if len(self.fuc) > 0:
            self.fuc.pop()

    def new_tot(self):
        self.tot += 1