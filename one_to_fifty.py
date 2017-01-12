#!/usr/bin/env python

def sum_multiples_of_three_and_five(limit=10):
    total = 0
    # for i in range(10):
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    print 'sum of multiples of three and five below %d : %d' % (limit, total)

def sum_even_fibonacci_terms(limit=10):
    total = 0
    first = 0
    second = 1
    term = 0
    while term < limit:
        term = first + second
        if term % 2 == 0:
            total += term
        first = second
        second = term


    print 'sum of even fibonacci terms where term < %d : %d' % (limit, total)

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def highest_prime_factor(number):
    n = number
    factors = []
    i = 2
    while i * i < n:
        if n % i == 0:
            n /= i
        i += 1
    print 'highest prime factor of %d : %d' % (number, n)

def largest_palindrome_of_product(factor_digits=2):
    products = []
    for a in range(1, 10**factor_digits):
        for b in range(1, 10**factor_digits):
            product = a * b
            print product
            products.append(product)
    print products



def main():
    print 'problem 1'
    # sum_multiples_of_three_and_five(limit=10)
    sum_multiples_of_three_and_five(limit=1000)

    print 'problem 2'
    # sum_even_fibonacci_terms(limit=10)
    sum_even_fibonacci_terms(limit=4000000)

    print 'problem 3'
    # highest_prime_factor(13195)
    highest_prime_factor(600851475143)

    print 'problem 4'
    largest_palindrome_of_product()

if __name__ == '__main__':
    main()
