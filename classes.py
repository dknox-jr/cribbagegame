class Player():
    def __init__(self, turn=False, dealer=False, score=0):
        self.score = score
        self.dealer = dealer
        self.turn = turn
        self.hand = []
        self.crib = []

    def altturn(self):
        if self.turn == False:
            self.turn = True
        elif self.turn == True:
            self.turn = False

current_player = Player(turn=False, dealer=False, score=0)


class Bot():
    def __init__(self, turn=False, dealer=False, score=0):
        self.score = score
        self.dealer = dealer
        self.turn = turn
        self.hand = []
        self.crib = []

    def altturn(self):
        if self.turn == True:
            self.turn = False
        elif self.turn == False:
            self.turn = True

opponent = Bot(turn=False, dealer=False, score=0)


class Round():
    def __init__(self, rid=0, fuc=None, lcp=None, tot=0):
        self.rid = rid
        self.lcp = lcp
        self.fuc = fuc
        self.tot = tot