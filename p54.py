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
        # print self.values
        # print self.suits
        # print self.counts

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return str(self)

    def score(self):
        if self.is_royal_straight_flush():
            return 1000
        elif self.is_straight_flush():
            return STRAIGHTS.index(self.values) + 900
        elif self.is_four_of_a_kind():
            score = 800
            for k,v in self.counts.items():
                if v == 1:
                    score += k
                if v == 4:
                    score += k * 4
            return score
        elif self.is_full_house():
            return sum(self.values) + 700
        elif self.is_flush():
            return sum(self.values) + 600
        elif self.is_straight():
            return STRAIGHTS.index(self.values) + 500
        elif self.is_three_of_a_kind():
            score = 400
            for k,v in self.counts.items():
                if v == 1:
                    score += k
                if v == 3:
                    score += k * 3
            return score
        elif self.is_two_pair():
            score = 300
            for k,v in self.counts.items():
                if v == 1:
                    score += k
                if v == 2:
                    score += k * 2
            return score
        elif self.is_pair():
            score = 200
            for k,v in self.counts.items():
                if v == 1:
                    score += k
                if v == 2:
                    score += k * 2
            return score
        return self.values[-1]

    def beats(self, other):
        if self.score() > other.score():
            return True
        if self.score() == other.score():
            for i in range(5):
                if self.values[i] > self.values[i]:
                    return True
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
print 'RSF', rsf1, rsf1.score()
print 'RSF', rsf2, rsf2.score()

sf1 = Hand([ Card('KC'), Card('QC'), Card('JC'), Card('TC'), Card('9C') ])
sf2 = Hand([ Card('AC'), Card('2C'), Card('3C'), Card('4C'), Card('5C') ])

print 'SF', sf1, sf1.score()
print 'SF', sf2, sf2.score()
foak1 = Hand([ Card('AC'), Card('AD'), Card('AH'), Card('AS'), Card('5C') ])
foak2 = Hand([ Card('KC'), Card('KD'), Card('KH'), Card('KS'), Card('5C') ])

print 'FOAK', foak1, foak1.score()
print 'FOAK', foak2, foak2.score()

fh1 = Hand([ Card('AC'), Card('AD'), Card('AH'), Card('KS'), Card('KC') ])
fh2 = Hand([ Card('AC'), Card('AD'), Card('KH'), Card('KS'), Card('KC') ])
print 'FH', fh1, fh1.score()
print 'FH', fh2, fh2.score()

s1 = Hand([ Card('2S'), Card('3S'), Card('4C'), Card('5D'), Card('6C') ])
s2 = Hand([ Card('AC'), Card('2S'), Card('3C'), Card('4D'), Card('5C') ])
print 'S', s1, s1.score()
print 'S', s2, s2.score()

toak1 = Hand([ Card('AC'), Card('AS'), Card('AD'), Card('4D'), Card('5C') ])
toak2 = Hand([ Card('KC'), Card('KS'), Card('KD'), Card('4D'), Card('5C') ])
print 'TOAK', toak1, toak1.score()
print 'TOAK', toak2, toak2.score()

tp1 = Hand([ Card('AC'), Card('AS'), Card('3C'), Card('3D'), Card('5C') ])
tp2 = Hand([ Card('KC'), Card('KS'), Card('3C'), Card('3D'), Card('5C') ])
print 'TP', tp1, tp1.score()
print 'TP', tp2, tp2.score()

p1 = Hand([ Card('AC'), Card('AS'), Card('2C'), Card('3D'), Card('5C') ])
p2 = Hand([ Card('KC'), Card('KS'), Card('2C'), Card('3D'), Card('5C') ])
print 'P', p1, p1.score()
print 'P', p2, p2.score()

hc1 = Hand([ Card('AC'), Card('KS'), Card('2C'), Card('3D'), Card('5C') ])
hc2 = Hand([ Card('KC'), Card('QS'), Card('2C'), Card('3D'), Card('5C') ])
print 'HC', hc1, hc1.score()
print 'HC', hc2, hc2.score()

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





count_p1_wins = 0
for line in read_file('p54.txt'):
    cards = line.split()
    p1 = Hand([ Card(c) for c in cards[:5] ])
    p2 = Hand([ Card(c) for c in cards[5:] ])
    if p1.beats(p2):
        count_p1_wins += 1
        print '%s %3d > %s %3d' % (p1, p1.score(), p2, p2.score())
print count_p1_wins
