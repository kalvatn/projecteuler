#!/usr/bin/env python

import re
import math
import time

from fractions import gcd
from operator import mul

from itertools import combinations

def read_file(filename):
    return [ line.strip() for line in open(filename) ]

def convert_lines_to_number_matrix(lines):
    return [ [ int(x) for x in line.split() ] for line in lines ]

def print_number_matrix(matrix, digit_size=1):
    for row in matrix:
        print ' '.join([ str(x).zfill(digit_size) for x in row ])

def integer_combinations(numbers, number_of_vars, target_sum=None):
    if target_sum is not None:
        return [ c for c in combinations(numbers, number_of_vars) if sum(c) == target_sum ]
    return [ c for c in combinations(numbers, number_of_vars)]

assert len(integer_combinations([1,2], 2, target_sum=0)) == 0
assert len(integer_combinations([1,2], 2, target_sum=3)) == 1
assert len(integer_combinations([10, 2, 1, 9], 2, target_sum=11)) == 2

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

assert is_prime(2)
assert is_prime(3)

def lowest_common_multiple(a, b):
    return a * b // gcd(a, b)

def no_remainder(number, divisor):
    return number % divisor == 0

def is_even(number):
    return no_remainder(number, 2)

def is_odd(number):
    return not is_even(number)

def is_palindrome(x):
    string = str(x)
    length = len(string)
    if length == 1:
        return True
    if is_even(length):
        middle = length / 2
        left = string[:middle]
        right = ''.join(reversed(string[middle:]))
    else:
        middle = length // 2
        left = string[:middle]
        right = ''.join(reversed(string[middle+1:]))
    return left == right

assert is_palindrome(1)
assert is_palindrome(11)
assert is_palindrome(9009)
assert is_palindrome(333)
assert is_palindrome(90009)

def print_answer(problem_number, description, answer):
    print 'problem %03d ; %150s : %s' % (problem_number, description, answer)

def problem1(limit=10):
    total = 0
    for i in range(limit):
        if no_remainder(i, 3) or no_remainder(i, 5):
            total += i
    return total

def problem2(limit=10):
    total = 0
    first = 0
    second = 1
    term = 0
    while term < limit:
        term = first + second
        if is_even(term):
            total += term
        first = second
        second = term
    return total

def problem3(number):
    n = number
    i = 2
    while i * i < n:
        if no_remainder(n, i):
            n /= i
        i += 1
    return n

def problem4(factor_digits=2):
    palindromes = []
    numbers = range(1, 10**factor_digits)
    for a in numbers:
        for b in numbers:
            product = a * b
            if is_palindrome(product):
                palindromes.append(product)
    return max(palindromes)

def problem5(limit=10):
    return reduce(lowest_common_multiple, range(1, limit+1))

def problem6(limit=10):
    sum_squares = 0
    number_sum = 0
    for i in range(1, limit+1):
        sum_squares += i ** 2
        number_sum += i
    square_sum = number_sum ** 2
    difference = sum_squares - square_sum
    return abs(difference)

def problem7(n):
    primes_found = []
    i = 1
    while len(primes_found) < n:
        if is_prime(i):
            primes_found.append(i)
        i += 1
    return primes_found[-1]

def problem8(adjacent_digits=4):
    number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
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

def problem9(target_sum):
    for a,b,c in integer_combinations(range(target_sum+1), 3, target_sum=target_sum):
        if a**2 + b**2 == c**2:
            return a * b * c

def problem10(limit=10):
    total = 0
    for i in range(limit):
        if is_prime(i):
            total += i
    return total

def matrix_groups_horizontal(matrix, group_size=2):
    groups = []

    length = len(matrix)
    for i in range(length):
        row = matrix[i]
        for j in range(length-(group_size-1)):
            groups.append(row[j:j+group_size])
    return groups

def matrix_groups_vertical(matrix, group_size=2):
    groups = []

    length = len(matrix)
    for i in range(length):
        for j in range(length-(group_size-1)):
            col = []
            for k in range(j, j+group_size):
                col.append(matrix[k][i])
            groups.append(col)
    return groups

def matrix_groups_diagonal_left_to_right(matrix, group_size=2):
    groups = []
    length = len(matrix)
    for i in range(length-(group_size-1)):
        for j in range(length-(group_size-1)):
            group = []
            for k in range(group_size):
                group.append(matrix[j+k][i+k])
            groups.append(group)
    return groups

def matrix_groups_diagonal_right_to_left(matrix, group_size=2):
    groups = []
    length = len(matrix)
    for i in range(length-1, group_size-2, -1):
        for j in range(length-(group_size-1)):
            group = []
            for k in range(group_size):
                group.append(matrix[i-k][j+k])
            groups.append(group)
    return groups



def problem11():
    lines = read_file('problem11_input.txt')
    # lines = read_file('problem11_test_input.txt')
    matrix = convert_lines_to_number_matrix(lines)

    greatest_product = ([], 0)
    for group in matrix_groups_horizontal(matrix, group_size=4):
        product = reduce(mul, group)
        if product > greatest_product[1]:
            greatest_product = (group, product)
        # print 'horizontal', group, product

    for group in matrix_groups_vertical(matrix, group_size=4):
        product = reduce(mul, group)
        if product > greatest_product[1]:
            greatest_product = (group, product)
        # print 'vertical', group, product

    for group in matrix_groups_diagonal_left_to_right(matrix, group_size=4):
        product = reduce(mul, group)
        if product > greatest_product[1]:
            greatest_product = (group, product)
        # print 'diagonal left-to-right', group, product

    for group in matrix_groups_diagonal_right_to_left(matrix, group_size=4):
        product = reduce(mul, group)
        if product > greatest_product[1]:
            greatest_product = (group, product)
        # print 'diagonal left-to-right', group, product
    # print_number_matrix(matrix, digit_size=2)
    return greatest_product



def problem12(min_divisors):
    divisors = []
    i = 1
    n = 0
    while len(divisors) < min_divisors:
        n = n + i
        divisors = []

        for x in xrange(1, int(n**0.5) + 1):
            if no_remainder(n, x):
                divisors.append(x)
                divisors.append(n / x)
        i += 1
    return n


def problem13():
    total = 0
    lines = read_file('problem13_input.txt')
    for line in lines:
        total += int(line)
    return str(total)[0:10]



def collatz_sequence(n, seq=[]):
    seq.append(n)
    if n == 1:
        return seq
    if is_even(n):
        return collatz_sequence(n/2, seq)
    return collatz_sequence(n * 3 + 1, seq)

# print collatz_sequence(13)

def problem14():
    longest_sequence = []
    for i in range(1, 1000000):
        seq = collatz_sequence(i, seq=[])
        if len(seq) > len(longest_sequence):
            longest_sequence = seq
            # print 'new longest %d : %d' % (seq[0], len(seq))
    return (longest_sequence[0], len(longest_sequence))

def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def problem15(grid_size):
    return binomial_coefficient(2 * grid_size, grid_size)


def problem16():
    number = 2**1000
    return sum( [ int(c) for c in str(number) ] )


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


def count_letters(s):
    return len(re.sub('[\W]', '', s))


def problem17(limit=1000):
    total_letters = 0
    for i in range(1, limit+1):
        number_as_words = number_to_words(i)
        letter_count = count_letters(number_as_words)
        total_letters += letter_count
        # print '%04d - %35s (%02d) - %5d' % (i, number_as_words, letter_count, total_letters)
    return total_letters

assert problem17(limit=5) == 19

assert count_letters(number_to_words(342)) == 23
assert count_letters(number_to_words(115)) == 20


class Node(object):
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

def problem18():
    lines = read_file('problem18_input.txt')
    lines = read_file('problem18_test_input.txt')
    matrix = convert_lines_to_number_matrix(lines)
    # i = len(matrix) * 2
    # for line in lines:
    #     print (i-len(line)/2) * ' ' + line

    nodes = [ [ Node(x, y, matrix[y][x]) for x in range(len(matrix[y])) ] for y in range(len(matrix)) ]

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

def problem19():
    months = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]
    days = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]

    def is_leap(year):
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
            if is_leap(year):
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


        if no_remainder(new_day_of_week, len(days)+1):
            new_day_of_week = 1
            new_week += 1
            new_day_of_week = 1
        if no_remainder(new_month, len(months)+1):
            new_month = 1
            new_year += 1
            new_day_of_year = 1
            new_week = 1

        return new_year, new_month, new_day_of_month, new_week, new_day_of_week, new_day_of_year

    assert increment_yy_mm_dd(1901, 1, 1, 1, 1, 1) == (1901, 1, 2, 1, 2, 2)
    assert increment_yy_mm_dd(1901, 1, 2, 1, 2, 2) == (1901, 1, 3, 1, 3, 3)
    assert increment_yy_mm_dd(1901, 1, 3, 1, 3, 3) == (1901, 1, 4, 1, 4, 4)
    assert increment_yy_mm_dd(1901, 1, 4, 1, 4, 4) == (1901, 1, 5, 1, 5, 5)
    assert increment_yy_mm_dd(1901, 1, 5, 1, 5, 5) == (1901, 1, 6, 1, 6, 6)
    assert increment_yy_mm_dd(1901, 1, 6, 1, 6, 6) == (1901, 1, 7, 1, 7, 7)
    assert increment_yy_mm_dd(1901, 1, 7, 1, 7, 7) == (1901, 1, 8, 2, 1, 8)
    assert increment_yy_mm_dd(1901, 12, 31, 52, 7, 365) == (1902, 1, 1, 1, 1, 1)

    count_sundays = 0
    year, month, day_of_month, week, day_of_week, day_of_year = increment_yy_mm_dd(1899, 12, 31, 52, 7, 365)

    # print '%4d-%02d-%02d, %10s, %10s %2d%s, week %2d, day of year : %d' % (year, month, day_of_month, days[day_of_week-1], months[month-1], day_of_month, ordinal_number_suffix(day_of_month), week, day_of_year)
    while year <= 2000:
        year, month, day_of_month, week, day_of_week, day_of_year = increment_yy_mm_dd(year, month, day_of_month, week, day_of_week, day_of_year)
        # print '%4d-%02d-%02d, %10s, %10s %2d%s, week %2d, day of year : %d' % (year, month, day_of_month, days[day_of_week-1], months[month-1], day_of_month, ordinal_number_suffix(day_of_month), week, day_of_year)
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

assert problem20(number=10) == 27

def main():
    # print_answer(1, 'sum of multiples of three and five below one thousand', problem1(1000))
    # print_answer(2, 'sum of even fibonacci terms where term is less than four million', problem2(limit=4000000))
    # print_answer(3, 'highest prime factor of 600851475143', problem3(600851475143))
    # print_answer(4, 'largest palindrome made from the product of two three-digit numbers', problem4(factor_digits=3))
    # print_answer(5, 'lowest number which is evenly divisible by all numbers from 1 to 20', problem5(limit=20))
    # print_answer(6, 'the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum', problem6(limit=100))
    # print_answer(7, 'the 10 001st prime number', problem7(10001))
    # print_answer(8, 'value of the thirteen adjacent digits in the 1000-digit number that have the greatest product', problem8(adjacent_digits=13))
    # print_answer(9, 'product of Pythagorean triplet for which a + b + c = 1000', problem9(1000))
    # print_answer(10, 'sum of all primes below two million', problem10(limit=2000000))
    # print_answer(11, 'the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid', problem11())
    # print_answer(12, 'value of the first triangle number to have over five hundred divisors', problem12(500))
    # print_answer(13, 'first ten digits of the sum of the 50 one-hundred digit numbers (problem13_input.txt)', problem13())
    # print_answer(14, 'starting number, under one million, produces the longest collatz chain', problem14())
    # print_answer(15, 'number of paths through a 20x20 grid only moving right and down', problem15(20))
    # print_answer(16, 'What is the sum of the digits of the number 2**1000', problem16())
    # print_answer(17, 'If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?', problem17())
    # print_answer(18, 'Find the maximum total from top to bottom of the triangle below', problem18())
    # print_answer(18, 'Find the maximum total from top to bottom of the triangle below', problem18())
    # print_answer(19, 'How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?', problem19())
    print_answer(20, 'Find the sum of the digits in the number 100! (factorial)', problem20())



if __name__ == '__main__':
    main()
