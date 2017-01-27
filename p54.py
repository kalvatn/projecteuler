from lib.util import read_file

SUITS = [ 'H', 'C', 'S', 'D' ]
VALUES = {
    'T' : 10,
    'J' : 11,
    'Q' : 12,
    'K' : 13,
    'A' : 14
}

STRAIGHTS = [ [2, 3, 4, 5, 14] ]
for i in range(2, 11):
    STRAIGHTS += [ range(i, i+5) ]

class Card(object):
    def __init__(self, c):
        self.c = c
        if c[0] in '23456789':
            self.value = int(c[0])
        else:
            self.value = VALUES[c[0]]
        self.suit = c[1]

    def __str__(self):
        return self.c

    def __repr__(self):
        return str(self)

assert Card('AH').value == 14
assert Card('TH').value == 10
assert Card('TH').suit == 'H'

class Hand(object):
    def __init__(self, cards):
        if len(cards) != 5:
            raise ValueError('hand must have five cards')
        self.cards = cards
        self.values = sorted([ c.value for c in self.cards ])
        self.suits = [ c.suit for c in self.cards ]
        self.counts = {v: 0 for v in self.values}
        for c in self.cards:
            self.counts[c.value] += 1
        self.name = 'HC'
        self.score = self.calc_score()

    def __str__(self):
        return '%s' % (str(self.cards))

    def __repr__(self):
        return str(self)

    def calc_score(self):
        if self.is_royal_straight_flush():
            self.name = 'RSF'
            return 1000
        elif self.is_straight_flush():
            self.name = 'SF'
            return STRAIGHTS.index(self.values) + 900
        elif self.is_four_of_a_kind():
            score = 800
            for k,v in self.counts.items():
                if v == 4:
                    score += k * 4
            self.name = 'FOAK'
            return score
        elif self.is_full_house():
            self.name = 'FH'
            score = 661
            for k,v in self.counts.items():
                if v == 3:
                    score += 3 * k
            return score
        elif self.is_flush():
            self.name = 'F'
            return sum(self.values) + 600
        elif self.is_straight():
            self.name = 'S'
            return STRAIGHTS.index(self.values) + 500
        elif self.is_three_of_a_kind():
            score = 400
            for k,v in self.counts.items():
                if v == 1:
                    score += k
                if v == 3:
                    score += k * 3
            self.name = 'TOAK'
            return score
        elif self.is_two_pair():
            score = 156
            for k,v in self.counts.items():
                # if v == 1:
                #     score += k
                if v == 2:
                    score += k * 10
            self.name = 'TP'
            return score
        elif self.is_pair():
            score = 15
            for k,v in self.counts.items():
                # if v == 1:
                #     score += k
                if v == 2:
                    score += k * 10
            self.name = 'P'
            return score
        return self.values[-1]

    def beats(self, other):
        if self.score > other.score:
            return True
        if self.score == other.score:
            for i in range(4, 0, -1):
                if self.values[i] == other.values[i]:
                    continue
                return self.values[i] > other.values[i]
        return False

    def has_count(self, n):
        return n in self.counts.values()

    def is_royal_straight_flush(self):
        return self.is_straight_flush() and self.values[-2] == 13

    def is_straight_flush(self):
        return self.is_flush() and self.is_straight()

    def is_four_of_a_kind(self):
        return self.has_count(4)

    def is_full_house(self):
        return self.has_count(3) and self.has_count(2)

    def is_flush(self):
        return len(set(self.suits)) == 1

    def is_straight(self):
        return sorted(self.values) in STRAIGHTS

    def is_three_of_a_kind(self):
        return self.has_count(3)

    def has_n_pair(self, n):
        count = 0
        for k, v in self.counts.items():
            if v == 2:
                count += 1
        return count == n

    def is_two_pair(self):
        return self.has_n_pair(2)

    def is_pair(self):
        return self.has_n_pair(1)


rsf1 = Hand([ Card('TC'), Card('JC'), Card('QC'), Card('KC'), Card('AC') ])
rsf2 = Hand([ Card('TH'), Card('JH'), Card('QH'), Card('KH'), Card('AH') ])

sf1 = Hand([ Card('KC'), Card('QC'), Card('JC'), Card('TC'), Card('9C') ])
sf2 = Hand([ Card('AC'), Card('2C'), Card('3C'), Card('4C'), Card('5C') ])

foak1 = Hand([ Card('AC'), Card('AD'), Card('AH'), Card('AS'), Card('5C') ])
foak2 = Hand([ Card('KC'), Card('KD'), Card('KH'), Card('KS'), Card('5C') ])

fh1 = Hand([ Card('AC'), Card('AD'), Card('AH'), Card('KS'), Card('KC') ])
fh2 = Hand([ Card('AC'), Card('AD'), Card('KH'), Card('KS'), Card('KC') ])

s1 = Hand([ Card('2S'), Card('3S'), Card('4C'), Card('5D'), Card('6C') ])
s2 = Hand([ Card('AC'), Card('2S'), Card('3C'), Card('4D'), Card('5C') ])

toak1 = Hand([ Card('AC'), Card('AS'), Card('AD'), Card('4D'), Card('5C') ])
toak2 = Hand([ Card('KC'), Card('KS'), Card('KD'), Card('4D'), Card('5C') ])

tp1 = Hand([ Card('AC'), Card('AS'), Card('3C'), Card('3D'), Card('5C') ])
tp2 = Hand([ Card('KC'), Card('KS'), Card('3C'), Card('3D'), Card('5C') ])

p1 = Hand([ Card('AC'), Card('AS'), Card('2C'), Card('3D'), Card('5C') ])
p2 = Hand([ Card('KC'), Card('KS'), Card('2C'), Card('3D'), Card('5C') ])

hc1 = Hand([ Card('AC'), Card('KS'), Card('2C'), Card('3D'), Card('5C') ])
hc2 = Hand([ Card('KC'), Card('QS'), Card('2C'), Card('3D'), Card('5C') ])

assert rsf1.is_royal_straight_flush()
assert rsf2.is_royal_straight_flush()
assert not rsf1.beats(rsf2)

assert sf1.is_straight_flush()
assert sf2.is_straight_flush()
assert sf1.beats(sf2)

assert foak1.is_four_of_a_kind()
assert foak2.is_four_of_a_kind()
assert foak1.beats(foak2)

assert fh1.is_full_house()
assert fh2.is_full_house()
assert fh1.beats(fh2)

assert s1.is_straight()
assert s2.is_straight()
assert s1.beats(s2)

assert toak1.is_three_of_a_kind()
assert toak2.is_three_of_a_kind()
assert toak1.beats(toak2)

assert tp1.is_two_pair()
assert tp2.is_two_pair()
assert tp1.beats(tp2)

assert p1.is_pair()
assert p2.is_pair()
assert p1.beats(p2)

assert hc1.beats(hc2)


def create_hand(s):
    return Hand([ Card(c) for c in s.split() ])





test_hands = [
    (create_hand('5H 5C 6S 7S KD'), create_hand('2C 3S 8S 8D TD')), #p2
    (create_hand('5D 8C 9S JS AC'), create_hand('2C 5C 7D 8S QH')), #p1
    (create_hand('2D 9C AS AH AC'), create_hand('3D 6D 7D TD QD')), #p2
    (create_hand('4D 6S 9H QH QC'), create_hand('3D 6D 7H QD QS')), #p1
    (create_hand('2H 2D 4C 4D 4S'), create_hand('3C 3D 3S 9S 9D')), #p1

    (create_hand('6D 7C 5D 5H 3S'), create_hand('5C JC 2H 5S 3D')), #p1
    ]
# for hands in test_hands:
#     print hands[0], hands[1], hands[0].score, hands[1].score, hands[0].name, hands[1].name
assert test_hands[0][1].beats(test_hands[0][0])
assert test_hands[1][0].beats(test_hands[1][1])
assert test_hands[2][1].beats(test_hands[2][0])
assert test_hands[3][0].beats(test_hands[3][1])
assert test_hands[4][0].beats(test_hands[4][1])
assert test_hands[5][1].beats(test_hands[5][0])






count_p1_wins = 0
count_p2_wins = 0
import time
for line in read_file('p54.txt'):
    cards = line.split()
    p1 = Hand([ Card(c) for c in cards[:5] ])
    p2 = Hand([ Card(c) for c in cards[5:] ])
    # include_only = [ 'HC' ]

    # if p1.name in include_only and p2.name in include_only:
    if p1.beats(p2):
        count_p1_wins += 1
        # print 'player 1 wins : %s %20s vs %20s %s (%4s %3d > %3d %4s)' % (p1, p1.values, p2.values, p2, p1.name, p1.score, p2.score, p2.name)
    if p2.beats(p1):
        # print 'player 2 wins : %s %20s vs %20s %s (%4s %3d > %3d %4s)' % (p1, p1.values, p2.values, p2, p1.name, p1.score, p2.score, p2.name)
        count_p2_wins += 1
assert count_p1_wins + count_p2_wins == 1000
# print 'p1 : %d, p2 : %d' % (count_p1_wins, count_p2_wins)
print count_p1_wins
