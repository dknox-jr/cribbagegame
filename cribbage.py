import random


class Card():
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self, rank=0, suit=0):
        self.rank = rank
        self.suit = suit

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



    # def __str__(self):
    #     s = ""
    #     for i in range(len(self.cards)):
    #         s += ", " + str(self.cards[i])
    #     print s

aceofclubs = Card(0, 0)
aceofdiamonds = Card(0, 1)
aceofhearts = Card(0, 2)
aceofspades = Card(0, 3)

deuceofclubs = Card(1, 0)
deuceofdiamonds = Card(1, 1)
deuceofhearts = Card(1, 2)
deuceofspades = Card(1, 3)

threeofclubs = Card(2, 0)
threeofdiamonds = Card(2, 1)
threeofhearts = Card(2, 2)
threeofspades = Card(2, 3)

fourofclubs = Card(3, 0)
fourofdiamonds = Card(3, 1)
fourofhearts = Card(3, 2)
fourofspades = Card(3, 3)

fiveofclubs = Card(4, 0)
fiveofdiamonds = Card(4, 1)
fiveofhearts = Card(4, 2)
fiveofspades = Card(4, 3)

sixofclubs = Card(5, 0)
sixofdiamonds = Card(5, 1)
sixofhearts = Card(5, 2)
sixofspades = Card(5, 3)

sevenofclubs = Card(6, 0)
sevenofdiamonds = Card(6, 1)
sevenofhearts = Card(6, 2)
sevenofspades = Card(6, 3)

eightofclubs = Card(7, 0)
eightofdiamonds = Card(7, 1)
eightofhearts = Card(7, 2)
eightofspades = Card(7, 3)

nineofclubs = Card(8, 0)
nineofdiamonds = Card(8, 1)
nineofhearts = Card(8, 2)
nineofspades = Card(8, 3)

tenofclubs = Card(9, 0)
tenofdiamonds = Card(9, 1)
tenofhearts = Card(9, 2)
tenofspades = Card(9, 3)

jackofclubs = Card(10, 0)
jackofdiamonds = Card(10, 1)
jackofhearts = Card(10, 2)
jackofspades = Card(10, 3)

queenofclubs = Card(11, 0)
queenofdiamonds = Card(11, 1)
queenofhearts = Card(11, 2)
queenofspades = Card(11, 3)

kingofclubs = Card(12, 0)
kingofdiamonds = Card(12, 1)
kingofhearts = Card(12, 2)
kingofspades = Card(12, 3)

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



# card1 = cards.pop(random.randint(0, 51))
# card2 = cards.pop(random.randint(0, 50))
#
# print card1, card2
#
# if Card.__cmp__(card1, other=card2) == 1:
#     print "Card1 outranks card2."
# else:
#     print "Card2 outranks card1."
#
# random.shuffle(cards)
# print cards.pop()
# print cards.pop()
# print cards.pop()
