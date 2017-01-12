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

def is_palindrome(x):
    string = str(x)
    length = len(string)
    if length == 1:
        return True

    if length % 2 == 0:
        middle = length / 2
        left = string[:middle]
        right = ''.join(reversed(string[middle:]))
    else:
        middle = length // 2
        left = string[:middle]
        right = ''.join(reversed(string[middle+1:]))

    # print '%d : middle : %d, left "%s", right "%s"' % (x, middle, left, right)
    return left == right



assert is_palindrome(1)
assert is_palindrome(11)
assert is_palindrome(9009)
assert is_palindrome(333)
assert is_palindrome(90009)

def largest_palindrome_of_product(factor_digits=2):
    palindromes = []
    for a in range(1, 10**factor_digits):
        for b in range(1, 10**factor_digits):
            product = a * b
            if is_palindrome(product):
                palindromes.append(product)
                # print '%d * %d = %d' % (a, b, product)
    print 'largest palindrome made from the product of two %d-digit numbers : %d' % (factor_digits, max(palindromes))



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
    # largest_palindrome_of_product(factor_digits=2)
    largest_palindrome_of_product(factor_digits=3)

if __name__ == '__main__':
    main()
