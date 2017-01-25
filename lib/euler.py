#!/usr/bin/env python
import unittest

import math
import re

from fractions import gcd

from itertools import combinations
from itertools import permutations


MONTHS = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]
WEEKDAYS = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]

def number_combinations(numbers):
    return [ c for c in combinations(numbers, len(numbers))]

def integer_combinations(numbers, number_of_vars, target_sum=None):
    if target_sum is not None:
        return [ c for c in combinations(numbers, number_of_vars) if sum(c) == target_sum ]
    return [ c for c in combinations(numbers, number_of_vars)]

def permute(l, length=None):
    return permutations(l, r=length)


def get_proper_divisors(n):
    divisors = set()
    for x in xrange(1, int(n**0.5) + 1):
        if no_remainder(n, x):
            divisors.add(x)
            if x != 1:
                divisors.add(n / x)
    return [ d for d in sorted(divisors) ]



def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if is_even(n) or no_remainder(n, 3):
        return False

    i = 5
    while i * i <= n:
        if no_remainder(n, i) or no_remainder(n, (i + 2)):
            return False
        i = i + 6
    return True

def prime_seq(n):
    """ list of primes with length == n """
    return prime_seq_below(10**6)[:n]

def prime_seq_below(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
    # seq = []
    # i = 2
    # while len(seq) < n:
    #     if is_prime(i):
    #         seq.append(i)
    #     i += 1
    # # print seq
    # return seq

def square_seq(n):
    seq = []
    for i in range(1, n+1):
        seq.append(2 * i ** 2)
    # print seq
    return seq


def lowest_common_multiple(a, b):
    return a * b // gcd(a, b)

def greatest_common_denominator(a, b):
    return gcd(a, b)

def no_remainder(number, divisor):
    return number % divisor == 0

def is_even(number):
    return no_remainder(number, 2)

def is_odd(number):
    return not is_even(number)

def is_palindrome(x):
    return str(x) == ''.join(reversed(str(x)))


def fibonacci(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

def triangle_seq(n):
    seq = []
    for i in range(1, n+1):
        seq.append(int((0.5 * i) * (i + 1)))
    # print seq
    return seq

def pentagonal_seq(n):
    seq = []
    for i in range(1, n+1):
        seq.append(int( i * (3*i - 1) * 0.5))
    return seq

def hexagonal_seq(n):
    seq = []
    for i in range(1, n+1):
        seq.append(int(i * (2 * i - 1)))
    # print seq
    return seq


def collatz(n, lookup={}):
    seq = []
    x = n

    # print n, x, lookup[x]
    while True:
        # print n, seq
        if x in lookup and lookup[x]:
            seq = seq + lookup[x]
            break
        else:
            seq.append(x)
            if x == 1:
                break
            elif is_even(x):
                x = x / 2
            else:
                x = x * 3 + 1
    lookup[n] = seq
    # print n, seq
    return lookup[n]


assert collatz(40) == [40, 20, 10, 5, 16, 8, 4, 2, 1 ]

def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


number_words = {
    10 : [ 'zero', 'one' 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten' ],
    99 : [ 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety' ],
    10**2 : 'hundred',
    10**3 : 'thousand',
    10**4 : 'million',
    10**5 : 'billion'
}

def number_to_words(n):
    below_ten       = [ 'zero', 'one',    'two',    'three',    'four',     'five',     'six',     'seven',     'eight',    'nine' ]
    below_twenty    = [ 'ten',  'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',  'sixteen', 'seventeen', 'eighteen', 'nineteen' ]
    tens            = [                   'twenty', 'thirty',   'forty',   'fifty',    'sixty',   'seventy',   'eighty',   'ninety' ]

    scale       = [ 10**2,      10**3,      10**6,      10**9,      10**12,     10**15,         10**18,         10**21,         10**24 ]
    scale_short = [ 'hundred',  'thousand', 'million',  'billion',  'trillion', 'quadrillion',  'quintillion',  'sextillion',   'septillion' ]
    scale_long  = [ 'hundred',  'thousand', 'million',  'milliard', 'billion',  'billiard',     'trillion',     'trilliard',    'quadrillion' ]
    if n < 10:
        return below_ten[n]
    if n < 20:
        quot, remainder = divmod(n, 10)
        return below_twenty[remainder]
    if n < 100:
        quot, remainder = divmod(n, 10)
        if remainder == 0:
            number_string = tens[quot-2]
        else:
            number_string = '%s-%s' % (tens[quot-2], number_to_words(remainder))
        return number_string

    for i in range(len(scale)-1, 0, -1):
        scale_number = scale[i-1]
        if n < scale_number:
            continue
        quot, remainder = divmod(n, scale_number)
        scale_unit_name = scale_short[i-1]
        number_string = '%s %s' % (number_to_words(quot), scale_unit_name)
        if remainder > 0:
            if scale_number == 100:
                number_string += ' and'
            number_string += ' ' + number_to_words(remainder)
        # print number_string
        return number_string
    return None



def count_letters(s):
    return len(re.sub('[\W]', '', s))

def ordinal_number_suffix(number):
    if number < 10 or number > 20:
        number_string = str(number)
        if number_string.endswith('1'):
            return 'st'
        if number_string.endswith('2'):
            return 'nd'
        if number_string.endswith('3'):
            return 'rd'
    return 'th'

class TriangleNode(object):
    def __init__(self, x, y, value, left=None, right=None):
        self.x = x
        self.y = y
        self.value = value
        self.left = left
        self.right = right

    def children(self):
        if self.left and self.right:
            return [ self.left, self.right]
        return []

    def __str__(self):
        return '[%d][%d] : %d' % (self.x, self.y, self.value)

    def __repr__(self):
        return str(self)

def is_leap_year(year):
    if no_remainder(year, 4):
        if no_remainder(year, 100):
            if no_remainder(year, 400):
                return True
            else:
                return False
        else:
            return True
    return False





def increment_yy_mm_dd(year, month, day_of_month, week, day_of_week, day_of_year):
    new_year = year
    new_month = month
    new_week = week
    new_day_of_week = day_of_week + 1
    new_day_of_month = day_of_month + 1
    new_day_of_year = day_of_year + 1
    if month == 2:
        if is_leap_year(year):
            if no_remainder(day_of_month, 29):
                new_day_of_month = 1
                new_month += 1
        elif no_remainder(day_of_month, 28):
            new_day_of_month = 1
            new_month += 1
    else:
        if month in (4, 6, 9, 11) and no_remainder(day_of_month, 30):
            new_day_of_month = 1
            new_month += 1
        elif no_remainder(day_of_month, 31):
            new_day_of_month = 1
            new_month += 1


    if no_remainder(new_day_of_week, len(WEEKDAYS)+1):
        new_day_of_week = 1
        new_week += 1
        new_day_of_week = 1
    if no_remainder(new_month, len(MONTHS)+1):
        new_month = 1
        new_year += 1
        new_day_of_year = 1
        new_week = 1

    return new_year, new_month, new_day_of_month, new_week, new_day_of_week, new_day_of_year

def concatenated_product(number, max_f):
    products = []
    for f in range(1, max_f+1):
        products.append(number * f)
    # print products
    return int(''.join([ str(p) for p in products ]))

def pythagorean_triplet_sum_solutions(target_sum):
    return pythagorean_triplets_up_to(target_sum)[target_sum]

def pythagorean_triplets_up_to(limit):
    import time
    solutions = {}
    s = 0
    c = 5
    while c <= limit // 2 + 1:
        for b in range(4, c):
            for a in range(3, b):
                if a**2 + b**2 == c**2:
                    s = a + b + c
                    if s not in solutions:
                        solutions[s] = []
                    solutions[s].append((a,b,c))
        c += 1

    filtered = {}
    for k in sorted(solutions.keys()):
        if k <= limit:
            filtered[k] = sorted(solutions[k])
    return filtered

if __name__ == '__main__':
    assert fibonacci(10) == [ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    assert collatz(13) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert collatz(40) == [40, 20, 10, 5, 16, 8, 4, 2, 1 ]

    assert binomial_coefficient(4, 2) == 6

    assert len(integer_combinations([1,2], 2, target_sum=0)) == 0
    assert len(integer_combinations([1,2], 2, target_sum=3)) == 1
    assert len(integer_combinations([10, 2, 1, 9], 2, target_sum=11)) == 2

    assert count_letters('abcde') == 5
    assert count_letters('ab cd-e') == 5

    assert count_letters(number_to_words(342)) == 23
    assert count_letters(number_to_words(115)) == 20


    assert is_prime(2)
    assert is_prime(3)
    assert is_palindrome(1)
    assert is_palindrome(11)
    assert is_palindrome(9009)
    assert is_palindrome(333)
    assert is_palindrome(90009)


    assert ordinal_number_suffix(1) == 'st'
    assert ordinal_number_suffix(11) == 'th'
    assert ordinal_number_suffix(21) == 'st'
    assert ordinal_number_suffix(32) == 'nd'
    assert ordinal_number_suffix(33) == 'rd'

    assert number_to_words(44) == 'forty-four'
    assert number_to_words(56) == 'fifty-six'
    assert number_to_words(99) == 'ninety-nine'
    assert number_to_words(101) == 'one hundred and one'
    assert number_to_words(142) == 'one hundred and forty-two'
    assert number_to_words(2142) == 'two thousand one hundred and forty-two'
    assert number_to_words(3333) == 'three thousand three hundred and thirty-three'
    assert number_to_words(33142) == 'thirty-three thousand one hundred and forty-two'
    assert number_to_words(333142) == 'three hundred and thirty-three thousand one hundred and forty-two'
    assert number_to_words(333142) == 'three hundred and thirty-three thousand one hundred and forty-two'
    assert number_to_words(5333142) == 'five million three hundred and thirty-three thousand one hundred and forty-two'
    assert number_to_words(50333142) == 'fifty million three hundred and thirty-three thousand one hundred and forty-two'
    assert number_to_words(999333142) == 'nine hundred and ninety-nine million three hundred and thirty-three thousand one hundred and forty-two'
    assert number_to_words(1999333142) == 'one billion nine hundred and ninety-nine million three hundred and thirty-three thousand one hundred and forty-two'

    assert increment_yy_mm_dd(1901, 1, 1, 1, 1, 1) == (1901, 1, 2, 1, 2, 2)
    assert increment_yy_mm_dd(1901, 1, 2, 1, 2, 2) == (1901, 1, 3, 1, 3, 3)
    assert increment_yy_mm_dd(1901, 1, 3, 1, 3, 3) == (1901, 1, 4, 1, 4, 4)
    assert increment_yy_mm_dd(1901, 1, 4, 1, 4, 4) == (1901, 1, 5, 1, 5, 5)
    assert increment_yy_mm_dd(1901, 1, 5, 1, 5, 5) == (1901, 1, 6, 1, 6, 6)
    assert increment_yy_mm_dd(1901, 1, 6, 1, 6, 6) == (1901, 1, 7, 1, 7, 7)
    assert increment_yy_mm_dd(1901, 1, 7, 1, 7, 7) == (1901, 1, 8, 2, 1, 8)
    assert increment_yy_mm_dd(1901, 12, 31, 52, 7, 365) == (1902, 1, 1, 1, 1, 1)

    assert get_proper_divisors(220) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    assert get_proper_divisors(284) == [1, 2, 4, 71, 142]

    assert concatenated_product(9, 5) == 918273645
    assert concatenated_product(192, 3) == 192384576

    # assert pythagorean_triplet_sum_solutions(1000) == [(200, 375, 425)]
    # assert pythagorean_triplet_sum_solutions(120) == [(20,48,52), (24,45,51), (30,40,50)]
    # triplets = pythagorean_triplets_up_to(1000)
    # for s in sorted(triplets.keys()):
    #     print s, triplets[s]

    assert triangle_seq(10) == [ 1, 3, 6, 10, 15, 21, 28, 36, 45, 55 ]
    assert pentagonal_seq(10) == [ 1, 5, 12, 22, 35, 51, 70, 92, 117, 145 ]
    assert hexagonal_seq(10) == [ 1, 6, 15, 28, 45, 66, 91, 120, 153, 190 ]
    assert triangle_seq(285)[-1] == pentagonal_seq(165)[-1] == hexagonal_seq(143)[-1]

    primes = prime_seq(10**4)
    assert primes[0:10] == [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ]
    assert primes[999] == 7919
    assert primes[9999] == 104729
    # assert primes[99999] == 1299709

    assert square_seq(10) == [ 2, 8, 18, 32, 50, 72, 98, 128, 162, 200 ]

