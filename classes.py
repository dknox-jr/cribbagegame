class Player():
    def __init__(self, score=0, turn=0):
        self.score = score
        self.turn = turn
        self.hand = []

    def take_turn(self):
