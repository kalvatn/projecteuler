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





def problem1(limit=10):
    total = 0
    for i in range(limit):
        if euler.no_remainder(i, 3) or euler.no_remainder(i, 5):
            total += i
    return total


def problem2(limit=10):
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

def problem3(number):
    n = number
    i = 2
    while i * i < n:
        if euler.no_remainder(n, i):
            n /= i
        i += 1
    return n

def problem4(factor_digits=2):
    palindromes = []
    numbers = range(1, 10**factor_digits)
    for a in numbers:
        for b in numbers:
            product = a * b
            if euler.is_palindrome(product):
                palindromes.append(product)
    return max(palindromes)

def problem5(limit=10):
    return reduce(euler.lowest_common_multiple, range(1, limit+1))

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
        if euler.is_prime(i):
            primes_found.append(i)
        i += 1
    return primes_found[-1]

def problem8(adjacent_digits=4):
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

def problem9(target_sum):
    for a,b,c in euler.integer_combinations(range(target_sum+1), 3, target_sum=target_sum):
        if a**2 + b**2 == c**2:
            return a * b * c

def problem10(limit=10):
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

def problem12(min_divisors):
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

def problem14():
    longest_sequence = []
    for i in range(1, 1000000):
        seq = euler.collatz_sequence(i, seq=[])
        if len(seq) > len(longest_sequence):
            longest_sequence = seq
            # print 'new longest %d : %d' % (seq[0], len(seq))
    return (longest_sequence[0], len(longest_sequence))

def problem15(grid_size):
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

assert problem17(limit=5) == 19




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

assert problem20(number=10) == 27



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


def print_answer(problem_number, description, answer):
    print 'problem %03d ; %150s : %s' % (problem_number, description, answer)

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
    # print_answer(20, 'Find the sum of the digits in the number 100! (factorial)', problem20())
    # print_answer(21, 'Evaluate the sum of all the amicable numbers under 10000.', problem21())
    # print_answer(22, 'What is the total of all the name scores in the file?', problem22())
    print_answer(23, 'Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.', problem23())
    print_answer(24, 'What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?', problem24())
    print_answer(25, 'What is the index of the first term in the Fibonacci sequence to contain 1000 digits?', problem25())



if __name__ == '__main__':
    main()
