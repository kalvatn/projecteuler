#!/usr/bin/env python

import re
import math
import time

from operator import mul

from itertools import combinations
from itertools import permutations
from lib import euler
from lib import util

from string import ascii_lowercase as alphabet





def problem1(limit=1000):
    total = 0
    for i in range(limit):
        if euler.no_remainder(i, 3) or euler.no_remainder(i, 5):
            total += i
    return total


def problem2(limit=4000000):
    total = 0
    first = 0
    second = 1
    term = 0
    while term < limit:
        term = first + second
        if euler.is_even(term):
            total += term
        first = second
        second = term
    return total

def problem3(number=600851475143):
    n = number
    i = 2
    while i * i < n:
        if euler.no_remainder(n, i):
            n /= i
        i += 1
    return n

def problem4(factor_digits=3):
    palindromes = []
    numbers = range(1, 10**factor_digits)
    for a in numbers:
        for b in numbers:
            product = a * b
            if euler.is_palindrome(product):
                palindromes.append(product)
    return max(palindromes)

def problem5(limit=20):
    return reduce(euler.lowest_common_multiple, range(1, limit+1))

def problem6(limit=100):
    sum_squares = 0
    number_sum = 0
    for i in range(1, limit+1):
        sum_squares += i ** 2
        number_sum += i
    square_sum = number_sum ** 2
    difference = sum_squares - square_sum
    return abs(difference)

def problem7(n=10001):
    primes_found = []
    i = 1
    while len(primes_found) < n:
        if euler.is_prime(i):
            primes_found.append(i)
        i += 1
    return primes_found[-1]

def problem8(adjacent_digits=13):
    number = int(util.read_file(filename='problem08_input.txt')[0])
    # number = 12345678901234567890
    number_str = str(number)
    greatest_product = 0
    for i in range(len(number_str)-(adjacent_digits-1)):
        product = 1
        section = number_str[i:i+adjacent_digits]
        product = reduce(mul, [ int(x) for x in section ])
        if product > greatest_product:
            greatest_product = product
    return greatest_product

def problem9(target_sum=1000):
    solutions = euler.pythagorean_triplet_sum_solutions(target_sum=target_sum)
    return solutions[0], reduce(mul, solutions[0])

def problem10(limit=2000000):
    total = 0
    for i in range(limit):
        if euler.is_prime(i):
            total += i
    return total

def problem11():
    lines = util.read_file('problem11_input.txt')
    # lines = util.read_file('problem11_test_input.txt')
    matrix = util.convert_lines_to_number_matrix(lines)

    greatest_product = ([], 0)
    for group in util.matrix_groups_horizontal(matrix, group_size=4):
        product = reduce(mul, group)
        if product > greatest_product[1]:
            greatest_product = (group, product)
        # print 'horizontal', group, product

    for group in util.matrix_groups_vertical(matrix, group_size=4):
        product = reduce(mul, group)
        if product > greatest_product[1]:
            greatest_product = (group, product)
        # print 'vertical', group, product

    for group in util.matrix_groups_diagonal_left_to_right(matrix, group_size=4):
        product = reduce(mul, group)
        if product > greatest_product[1]:
            greatest_product = (group, product)
        # print 'diagonal left-to-right', group, product

    for group in util.matrix_groups_diagonal_right_to_left(matrix, group_size=4):
        product = reduce(mul, group)
        if product > greatest_product[1]:
            greatest_product = (group, product)
        # print 'diagonal left-to-right', group, product
    # print_number_matrix(matrix, digit_size=2)
    return greatest_product

def problem12(min_divisors=500):
    divisors = []
    i = 1
    n = 0
    while len(divisors) < min_divisors:
        n = n + i
        divisors = []

        for x in xrange(1, int(n**0.5) + 1):
            if euler.no_remainder(n, x):
                divisors.append(x)
                divisors.append(n / x)
        i += 1
    return n


def problem13():
    total = 0
    lines = util.read_file('problem13_input.txt')
    for line in lines:
        total += int(line)
    return str(total)[0:10]

def problem14(limit=10**6):
    longest_sequence = []

    numbers = xrange(2, limit)
    lookup = { i : [] for i in numbers }
    for i in numbers:
        seq = euler.collatz(i, lookup=lookup)
        if len(seq) > len(longest_sequence):
            longest_sequence = seq
            # print 'new longest %d : %d' % (seq[0], len(seq))
    return (longest_sequence[0], len(longest_sequence))


def problem15(grid_size=20):
    return euler.binomial_coefficient(2 * grid_size, grid_size)

def problem16():
    number = 2**1000
    return sum( [ int(c) for c in str(number) ] )

def problem17(limit=1000):
    total_letters = 0
    for i in range(1, limit+1):
        number_as_words = euler.number_to_words(i)
        letter_count = euler.count_letters(number_as_words)
        total_letters += letter_count
        # print '%04d - %35s (%02d) - %5d' % (i, number_as_words, letter_count, total_letters)
    return total_letters

# assert problem17(limit=5) == 19




def problem18():
    lines = util.read_file('problem18_input.txt')
    lines = util.read_file('problem18_test_input.txt')
    matrix = util.convert_lines_to_number_matrix(lines)
    # i = len(matrix) * 2
    # for line in lines:
    #     print (i-len(line)/2) * ' ' + line

    nodes = [ [ euler.TriangleNode(x, y, matrix[y][x]) for x in range(len(matrix[y])) ] for y in range(len(matrix)) ]

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            node = nodes[y][x]
            if y < len(matrix)-1:
                node.left = nodes[y+1][x]
                node.right = nodes[y+1][x+1]
            nodes.append(node)

    def get_path_with_maximum_sum(node, path):
        if node.left and node.right:
            left_path = get_path_with_maximum_sum(node.left, path)
            right_path = get_path_with_maximum_sum(node.right, path)
            if sum([ n.value for n in left_path]) > sum([ n.value for n in right_path ]):
                path = left_path + [ node ]
            else:
                path = right_path + [ node ]
            return path
        else:
            return path + [ node ]
    path = [ x for x in reversed(get_path_with_maximum_sum(nodes[0][0], [])) ]
    return sum([ n.value for n in path ]), [ n.value for n in path ]



def problem19():

    count_sundays = 0
    year, month, day_of_month, week, day_of_week, day_of_year = euler.increment_yy_mm_dd(1899, 12, 31, 52, 7, 365)

    # print '%4d-%02d-%02d, %10s, %10s %2d%s, week %2d, day of year : %d' % (year, month, day_of_month, euler.WEEKDAYS[day_of_week-1], euler.MONTHS[month-1], day_of_month, euler.ordinal_number_suffix(day_of_month), week, day_of_year)
    while year <= 2000:
        year, month, day_of_month, week, day_of_week, day_of_year = euler.increment_yy_mm_dd(year, month, day_of_month, week, day_of_week, day_of_year)
        # print '%4d-%02d-%02d, %10s, %10s %2d%s, week %2d, day of year : %d' % (year, month, day_of_month, euler.WEEKDAYS[day_of_week-1], euler.MONTHS[month-1], day_of_month, euler.ordinal_number_suffix(day_of_month), week, day_of_year)
        if day_of_week == 7:
            if day_of_month == 1 and 1901 <= year < 2001:
                count_sundays += 1
                # print 'number of sundays at the first of every month : %d' % count_sundays
        # time.sleep(0.5)

    return count_sundays


def problem20(number=100):
    factorial_sum = 1
    for i in range(number, 1, -1):
        factorial_sum *= i
    digit_sum = 0
    for c in str(factorial_sum):
        digit_sum += int(c)
    return digit_sum

# assert problem20(number=10) == 27



def problem21(limit=10000):
    amicable_numbers = set()
    divisors = {}
    for a in range(1, limit):
        if a not in divisors:
            divisors[a] = euler.get_proper_divisors(a)
    for a in range(1, limit):
        for b in range(1, limit):
            if a != b:
                if sum(divisors[b]) == a and sum(divisors[a]) == b:
                    amicable_numbers.add(a)
                    amicable_numbers.add(b)
    return sum(amicable_numbers)

def problem22():
    lines = [ re.sub('"', '', line).lower() for line in sorted(util.read_file(filename='problem22_input.txt')[0].split(','))]
    total = 0
    for i in range(0, len(lines)):
        name = lines[i]
        name_score = sum([ (alphabet.index(c)+1) for c in name ])
        total += name_score * (i+1)
        # print name, pos, name_score, name_score * pos
    return total

def problem23():
    abundant_numbers = []
    for i in range(1, 28123 + 1):
    # for i in range(12, 1000):
        divisors = euler.get_proper_divisors(i)
        divisor_sum = sum(divisors)
        is_abundant = divisor_sum > i
        if is_abundant:
            abundant_numbers.append(i)
            # print '%05d %150s %05d' % (i, divisors, divisor_sum)

    sums = set()
    for a in abundant_numbers:
        for b in abundant_numbers:
            sums.add(a + b)

    total = 0
    for i in range(1, 28123 + 1):
        if i not in sums:
            total += i
    return total



def problem24():
    numbers = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    perms = [ p for p in permutations(numbers) ]
    return ''.join(str(n) for n in perms[1000000-1])


def problem25(limit=1000):
    first = 0
    second = 1
    term = 0
    i = 1
    # print i, 1
    while len(str(term)) < limit:
        i += 1
        term = first + second
        first = second
        second = term
        # print i, term
    return i

def strip_trailing_zeroes(s):
    new_s = ''
    end = len(s)
    for i in range(len(s)-1, 0, -1):
        if s[i] == '0' and s[i-1] == '0':
            end = i
    return s[0:end]

def problem26(d=1000):
    longest = (0, 0)
    for i in range(1, d):
        remainders = []
        quotients = []
        length = 0
        remainder = 1

        while remainder:
            quotient, remainder = divmod(remainder, i)

            # print 'quotient : %d, remainder : %d' % (quotient, remainder)
            if remainder in remainders:
                length = len(quotients) - remainders.index(remainder)
                break
            remainders.append(remainder)
            quotients.append(quotient)
            remainder *= 10
        if length > longest[1]:
            longest = (i, length)
            # print 'new longest : 1/%d has length %d, quotients : %s' % (i, length, quotients)
    return longest


def problem27():
    prime = set()
    not_prime = set()
    a_limit = 1000
    b_limit = 1001

    def quadratic(n, a, b):
        return (n**2) + (a * n) + b
    longest = (0, 0, 0, [])
    for a in range(-a_limit, a_limit):
        for b in range(-b_limit, b_limit):
            chain = []
            n = 0
            while True:
                r = quadratic(n, a, b)
                if r not in prime:
                    if r not in not_prime:
                        if euler.is_prime(r):
                            prime.add(r)
                        else:
                            not_prime.add(r)
                if r in prime:
                    # print 'n=%4d, a=%3d, b=%3d = %d' % (n, a, b, r)
                    chain.append(r)
                else:
                    if len(chain) > len(longest[3]):
                        longest = (a, b, n, chain)
                        # print 'new longest (%d) a=%3d, b=%3d : %s' % (len(chain), a, b, chain)
                    break
                n += 1
    # print longest
    return longest[0] * longest[1]

def problem28(n=1001):
    matrix = [ [ 0 for x in range(n) ] for y in range(n) ]

    # util.print_number_matrix(matrix)
    x = n // 2
    y = n // 2
    y_dir = 1
    x_dir = -1
    size = n * n
    dy = 0
    dx = 0
    for i in range(1, size + 1):
        matrix[y][x] = i

        # util.print_number_matrix(matrix, digit_size=3)
        # print

        if x == y:
            # print 'x == y'
            x_dir *= -1
            dx = x_dir
            dy = 0
        else:
            if (x-1 + y) == n-1 and x > y > 0:
                # print 'x-1 + y % 10 == 0'
                dy = y_dir
                y_dir *= -1
                dx = 0
            elif (x + y) == n-1 and 0 < y > x:
                # print 'x+y % 10 == 0'
                dy = y_dir
                y_dir *= -1
                dx = 0

        y += dy
        x += dx

    diagonal_numbers = []

    for y in range(n):
        for x in range(n):
            if x == y or (x+y) == n-1:
                diagonal_numbers.append(matrix[y][x])

    # util.print_number_matrix(matrix, digit_size=4)

    # print 'diagonal numbers : %s ' % (diagonal_numbers)
    # print
    return sum(diagonal_numbers)





# assert problem28(n=5) == 101


def problem29(limit=100):
    terms = set()
    for a in range(2, limit+1):
        for b in range(2, limit+1):
            terms.add(a**b)


    # print [ t for t in sorted(terms) ]
    return len([ t for t in sorted(terms) ])

# assert problem29(limit=5) == len([ 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125 ])


def problem30(power=5):
    numbers = []
    for i in xrange(10, (9**power)*power):
        s = 0
        powered = [ int(c)**power for c in str(i) ]
        # print i, powered
        if sum(powered) == i:
            # print i, powered
            numbers.append(i)
    # print numbers
    return sum(numbers)

# assert problem30(power=4) == sum([ 1634, 8208, 9474 ])


def problem31(target=200):
    coins = [ 1, 2, 5, 10, 20, 50, 100, 200 ]
    combos = [ 0 ] * (target + 1)
    combos[0] = 1
    for coin in coins:
        for total in range(target + 1):
            if total >= coin:
                combos[total] += combos[total - coin]

    return combos[target]

def problem32():
    perms = set()
    for p in euler.permute(range(1, 10)):
        p_string = ''.join([ str(x) for x in p])
        perms.add(p_string)

    products = set()
    for a in range(2000):
        for b in range(2000):
            p = a * b
            if p not in products:
                c = str(a) + str(b) + str(p)
                if c in perms:
                    # print a, b, p, c
                    products.add(p)
    return sum(products)

def problem33():
    dp = 1
    np = 1
    for i in range(1, 10):
        for j in range(1, i):
            for k in range(1, j):
                if (k * 10 + i) * j == k * (i * 10 + j):
                    np *= k
                    dp *= j
    dp /= euler.greatest_common_denominator(np, dp)
    return dp

def problem34():
    factorials = {}
    found = set()
    for i in xrange(3, 10**5):
        i_fac_sum = 0
        for j in [ int(c) for c in reversed(str(i)) ]:
            if j not in factorials:
                j_fac = math.factorial(j)
                factorials[j] = j_fac

            i_fac_sum += factorials[j]
        if i_fac_sum == i:
            found.add(i)
            # print i, i_fac_sum

    return sum(found)

# problem34() == sum([ 145, 40585 ])


def problem35(limit=10**6):
    circular = set()
    primes = set()
    for i in range(limit):
        if euler.is_prime(i):
            primes.add(i)
    for prime in primes:
        digits = [ int(c) for c in str(prime) ]
        # print prime, digits
        is_circular = True

        rotations = [ int(r) for r in util.string_rotations(str(prime)) ]
        for candidate in rotations:
            if candidate not in primes:
                is_circular = False
        if is_circular:
            circular.add(prime)

    circular = sorted([ c for c in circular ])
    # print circular
    return len(circular)

# assert problem35(limit=10**2) == 13

def problem36(limit=10**6):
    palindromic_base2_and_10 = set()
    for i in range(limit):
        if euler.is_palindrome(i):
            binary = '{0:b}'.format(i)
            if euler.is_palindrome(binary):
                palindromic_base2_and_10.add((i, binary))
    # print palindromic_base2_and_10
    return sum([ p[0] for p in palindromic_base2_and_10])

# assert problem36(limit=10**3) == 1772

def problem37():

    primes = set()
    truncatable_primes = set()

    i = 1
    while len(truncatable_primes) < 11:
        if euler.is_prime(i):
            primes.add(i)
        i_str = str(i)
        if len(i_str) >= 2:

            is_truncatable = True
            for l in range(0, len(i_str)):
                lr = i_str[l:]
                rl = i_str[0:l+1]
                if not int(lr) in primes or not int(rl) in primes:
                    is_truncatable = False
                    break
            if is_truncatable:
                # print i, lr, rl
                truncatable_primes.add(i)
        i += 1
    # print truncatable_primes
    return sum(truncatable_primes)

def problem38():
    nine_digit_pandas = set()
    for p in euler.permute(range(1, 10)):
        nine_digit_pandas.add(int(''.join(map(str, list(p)))))

    numbers_to_check = set()
    for i in range(1, 5):
        for p in euler.permute(range(1, 10), i):
            numbers_to_check.add(int(''.join(map(str, list(p)))))
    # print numbers_to_check
    max_allowed = max(nine_digit_pandas)


    largest_product = (0, 0, 0)
    for i in numbers_to_check:
        f = 2
        p = 0

        while p <= max_allowed:
            p = euler.concatenated_product(i, f)
            if p > largest_product[2] and p in nine_digit_pandas:
                # print 'new largest : ', i, f, p
                largest_product = (i, f, p)
            f+=1
    return largest_product


def problem39(limit=1000):
    most_solutions = (0, 0)
    triplets_by_sum = euler.pythagorean_triplets_up_to(limit)
    for triplet_sum, solutions in triplets_by_sum.items():
        if len(solutions) > most_solutions[1]:
            most_solutions = (triplet_sum, len(solutions))
    return most_solutions


def problem40(limit=10**6):
    fraction = ''.join(map(str, xrange(1, limit)))
    assert fraction.startswith('123456789101112131415161718192021')
    assert fraction[21-1] == '5'
    assert fraction[12-1] == '1'
    total = 1
    for i in [ 1, 10, 10**2, 10**3, 10**4, 10**5, 10**6 ]:
        if i <= limit:
            digit = int(fraction[i-1])
            total *= digit
            # print 'digit #%d in fraction : %d' % (i, digit)
    return total


# problem40(1000)

def problem41():
    numbers_to_check = set()
    for i in range(1, 10):
        for p in euler.permute(range(1, i+1)):
            numbers_to_check.add(int(''.join(map(str, list(p)))))
    numbers_to_check = reversed(sorted(numbers_to_check))
    for i in numbers_to_check:
        if euler.is_prime(i):
            return i

def problem42():
    lines = [ re.sub('"', '', line).lower() for line in sorted(util.read_file(filename='problem42_input.txt')[0].split(','))]

    triangles = euler.triangle_seq(200)

    count = 0
    for name in lines:
        name_score = sum([ (alphabet.index(c)+1) for c in name ])
        if name_score in triangles:
            count += 1
            # print name, name_score, triangles.index(name_score) + 1
    return count

def problem43():
    numbers = set()
    divisors = [ 2, 3, 5, 7, 11, 13, 17 ]
    for p in euler.permute(range(0, 10)):
        n = ''.join(map(str, list(p)))
        candidate = True
        for i in range(1, len(n)-2):
            sub = int(n[i:i+3])
            if sub % divisors[i-1] != 0:
                candidate = False
                break
        if candidate:
            # print n
            numbers.add(int(n))
    return sum(numbers)



def print_answer(problem_number, description):
    start = time.time()
    answer = globals()['problem%d' % (problem_number)]()
    elapsed = time.time() - start

    print '%03d %170s %30s (%.2fs)' % (problem_number, description, answer, elapsed)

def main():
    """
    SLOW : 1-5s
    VERY SLOW : 5->10s
    EXTREMELY SLOW : 10s ->..
    """
    # print_answer(1, 'sum of multiples of three and five below one thousand')
    # print_answer(2, 'sum of even fibonacci terms where term is less than four million')
    # print_answer(3, 'highest prime factor of 600851475143')
    # print_answer(4, 'largest palindrome made from the product of two three-digit numbers')
    # print_answer(5, 'lowest number which is evenly divisible by all numbers from 1 to 20')
    # print_answer(6, 'the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum')
    # print_answer(7, 'the 10 001st prime number')
    # print_answer(8, 'value of the thirteen adjacent digits in the 1000-digit number that have the greatest product')
    # # print_answer(9, 'product of Pythagorean triplet for which a + b + c = 1000') # SLOW
    # # print_answer(10, 'sum of all primes below two million') # SLOW
    # print_answer(11, 'the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid')
    # # print_answer(12, 'value of the first triangle number to have over five hundred divisors') # SLOW
    # print_answer(13, 'first ten digits of the sum of the 50 one-hundred digit numbers (problem13_input.txt)')
    # # print_answer(14, 'starting number, under one million, produces the longest collatz chain') # VERY SLOW
    # print_answer(15, 'number of paths through a 20x20 grid only moving right and down')
    # print_answer(16, 'What is the sum of the digits of the number 2**1000')
    # print_answer(17, 'If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?')
    # print_answer(18, 'Find the maximum total from top to bottom of the triangle below')
    # print_answer(19, 'How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?')
    # print_answer(20, 'Find the sum of the digits in the number 100! (factorial)')
    # # print_answer(21, 'Evaluate the sum of all the amicable numbers under 10000.') # EXTREMELY SLOW
    # print_answer(22, 'What is the total of all the name scores in the file?')
    # # print_answer(23, 'Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.') # SLOW
    # print_answer(24, 'What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?')
    # print_answer(25, 'What is the index of the first term in the Fibonacci sequence to contain 1000 digits?')
    # print_answer(26, 'Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.')
    # print_answer(27, 'Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.') # SLOW
    # print_answer(28, 'What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?')
    # print_answer(29, 'How many distinct terms are in the sequence generated by ab for 2 <= a <= 100 and 2 <= b <= 100?')
    # print_answer(30, 'Find the sum of all the numbers that can be written as the sum of fifth powers of their digits')
    # print_answer(31, 'How many different ways can 2 pounds be made using any number of coins?')
    # # print_answer(32, 'Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.') # SLOW
    # print_answer(33, 'If the product of these four fractions is given in its lowest common terms, find the value of the denominator.')
    # print_answer(34, 'Find the sum of all numbers which are equal to the sum of the factorial of their digits.')
    # # print_answer(35, 'How many circular primes are there below one million?') # SLOW
    # print_answer(36, 'Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.')
    # # print_answer(37, 'Find the sum of the only eleven primes that are both truncatable from left to right and right to left.') # SLOW
    # print_answer(38, 'What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?') # VERY SLOW
    # print_answer(39, 'For which value of p <= 1000, is the number of solutions maximised?') # SLOW
    # print_answer(40, 'If dn represents the nth digit of the fractional part, find the value of the following expression; d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000')
    # print_answer(41, 'What is the largest n-digit pandigital prime that exists')
    # print_answer(42, 'how many are triangle words?')
    print_answer(43, 'Find the sum of all 0 to 9 pandigital numbers with this property.')







if __name__ == '__main__':
    main()
