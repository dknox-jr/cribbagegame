import random
class Card():
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self, rank=0, suit=0, value=0):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.ranks[self.rank] + " of " + self.suits[self.suit]

    def __cmp__(self, other):
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        return 0


class Deck():
    def __init__(self):
        self.cards = []
        for rank in range(0, 13):
            for suit in range(0, 4):
                self.cards.append(Card(rank, suit))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " + str(self.cards[i]) + ""
        print s

aceofclubs = Card(0, 0, 1)
aceofdiamonds = Card(0, 1, 1)
aceofhearts = Card(0, 2, 1)
aceofspades = Card(0, 3, 1)

deuceofclubs = Card(1, 0, 2)
deuceofdiamonds = Card(1, 1, 2)
deuceofhearts = Card(1, 2, 2)
deuceofspades = Card(1, 3, 2)

threeofclubs = Card(2, 0, 3)
threeofdiamonds = Card(2, 1, 3)
threeofhearts = Card(2, 2, 3)
threeofspades = Card(2, 3, 3)

fourofclubs = Card(3, 0, 4)
fourofdiamonds = Card(3, 1, 4)
fourofhearts = Card(3, 2, 4)
fourofspades = Card(3, 3, 4)

fiveofclubs = Card(4, 0, 5)
fiveofdiamonds = Card(4, 1, 5)
fiveofhearts = Card(4, 2, 5)
fiveofspades = Card(4, 3, 5)

sixofclubs = Card(5, 0, 6)
sixofdiamonds = Card(5, 1, 6)
sixofhearts = Card(5, 2, 6)
sixofspades = Card(5, 3, 6)

sevenofclubs = Card(6, 0, 7)
sevenofdiamonds = Card(6, 1, 7)
sevenofhearts = Card(6, 2, 7)
sevenofspades = Card(6, 3, 7)

eightofclubs = Card(7, 0, 8)
eightofdiamonds = Card(7, 1, 8)
eightofhearts = Card(7, 2, 8)
eightofspades = Card(7, 3, 8)

nineofclubs = Card(8, 0, 9)
nineofdiamonds = Card(8, 1, 9)
nineofhearts = Card(8, 2, 9)
nineofspades = Card(8, 3, 9)

tenofclubs = Card(9, 0, 10)
tenofdiamonds = Card(9, 1, 10)
tenofhearts = Card(9, 2, 10)
tenofspades = Card(9, 3, 10)

jackofclubs = Card(10, 0, 10)
jackofdiamonds = Card(10, 1, 10)
jackofhearts = Card(10, 2, 10)
jackofspades = Card(10, 3, 10)

queenofclubs = Card(11, 0, 10)
queenofdiamonds = Card(11, 1, 10)
queenofhearts = Card(11, 2, 10)
queenofspades = Card(11, 3, 10)

kingofclubs = Card(12, 0, 10)
kingofdiamonds = Card(12, 1, 10)
kingofhearts = Card(12, 2, 10)
kingofspades = Card(12, 3, 10)

cards = [aceofclubs, aceofdiamonds, aceofhearts, aceofspades,
         deuceofclubs, deuceofdiamonds, deuceofhearts, deuceofspades,
         threeofclubs, threeofdiamonds, threeofhearts, threeofspades,
         fourofclubs, fourofdiamonds, fourofhearts, fourofspades,
         fiveofclubs, fiveofdiamonds, fiveofhearts, fiveofspades,
         sixofclubs, sixofdiamonds, sixofhearts, sixofspades,
         sevenofclubs, sevenofdiamonds, sevenofhearts, sevenofspades,
         eightofclubs, eightofdiamonds, eightofhearts, eightofspades,
         nineofclubs, nineofdiamonds, nineofhearts, nineofspades,
         tenofclubs, tenofdiamonds, tenofhearts, tenofspades,
         jackofclubs, jackofdiamonds, jackofhearts, jackofspades,
         queenofclubs, queenofdiamonds, queenofhearts, queenofspades,
         kingofclubs, kingofdiamonds, kingofhearts, kingofspades]

