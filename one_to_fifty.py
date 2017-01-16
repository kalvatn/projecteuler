#!/usr/bin/env python

import math
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
    print 'problem %03d ; %80s : %s' % (problem_number, description, answer)

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
    print 'horizontal groups'
    for group in matrix_groups_horizontal(matrix, group_size=4):
        product = reduce(mul, group)
        if product > greatest_product[1]:
            greatest_product = (group, product)
        # print 'horizontal', group, product
    print 'greatest_product horizontal %s : %d' % (greatest_product[0], greatest_product[1])

    print 'vertical groups'
    for group in matrix_groups_vertical(matrix, group_size=4):
        product = reduce(mul, group)
        if product > greatest_product[1]:
            greatest_product = (group, product)
        # print 'vertical', group, product

    print 'greatest_product vertical %s : %d' % (greatest_product[0], greatest_product[1])

    print 'diagonal groups'
    for group in matrix_groups_diagonal_left_to_right(matrix, group_size=4):
        product = reduce(mul, group)
        if product > greatest_product[1]:
            greatest_product = (group, product)
        # print 'diagonal left-to-right', group, product

    print 'greatest_product diagonal left-to-right %s : %d' % (greatest_product[0], greatest_product[1])

    print 'diagonal groups'
    for group in matrix_groups_diagonal_right_to_left(matrix, group_size=4):
        product = reduce(mul, group)
        if product > greatest_product[1]:
            greatest_product = (group, product)
        # print 'diagonal left-to-right', group, product

    print 'greatest_product diagonal right-to-left %s : %d' % (greatest_product[0], greatest_product[1])

    # print_number_matrix(matrix, digit_size=2)
    return greatest_product


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
    print_answer(11, 'the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid', problem11())



if __name__ == '__main__':
    main()
