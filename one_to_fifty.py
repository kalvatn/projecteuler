#!/usr/bin/env python

import math
from fractions import gcd

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


def main():
    print_answer(1, 'sum of multiples of three and five below one thousand', problem1(1000))
    print_answer(2, 'sum of even fibonacci terms where term is less than four million', problem2(limit=4000000))
    print_answer(3, 'highest prime factor of 600851475143', problem3(600851475143))
    print_answer(4, 'largest palindrome made from the product of two three-digit numbers', problem4(factor_digits=3))
    print_answer(5, 'lowest number which is evenly divisible by all numbers from 1 to 20', problem5(limit=20))
    print_answer(6, 'the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum', problem6(limit=100))
    print_answer(7, 'the 10 001st prime number', problem7(10001))

if __name__ == '__main__':
    main()
