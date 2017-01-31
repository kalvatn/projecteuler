ONE             = 'I'
FIVE            = 'V'
TEN             = 'X'
FIFTY           = 'L'
HUNDRED         = 'C'
FIVE_HUNDRED    = 'D'
THOUSAND        = 'M'

DENARY_TO_ROMAN = {
    1   : ONE,
    5   : FIVE,
    10  : TEN,
    50  : FIFTY,
    100 : HUNDRED,
    500 : FIVE_HUNDRED,
    1000: THOUSAND,
}

ROMAN_TO_DENARY = {
    ONE             : 1,
    FIVE            : 5,
    TEN             : 10,
    FIFTY           : 50,
    HUNDRED         : 100,
    FIVE_HUNDRED    : 500,
    THOUSAND        : 1000,
}

def roman(number):
    """
    https://projecteuler.net/about=roman_numerals
    """
    if number in DENARY_TO_ROMAN:
        return DENARY_TO_ROMAN[number]

    if number <= 5:
        if number >= 4:
            return roman(1) + roman(5)
        return number * roman(1)
    if 5 <= number < 10:
        if number >= 9:
            return roman(1) + roman(10)
        return roman(5) + roman(number - 5)
    if 10 <= number < 50:
        if number >= 40:
            return roman(10) + roman(50) + roman(number - 40)
        return roman(10) + roman(number - 10)
    elif 50 <= number < 100:
        if number >= 90:
            return roman(10) + roman(100) + roman(number - 90)
        return roman(50) + roman(number - 50)
    elif 100 <= number < 500:
        if number >= 400:
            return roman(100) + roman(500) + roman(number - 400)
        return roman(100) + roman(number - 100)
    elif 500 <= number < 1000:
        if number >= 900:
            return roman(100) + roman(1000) + roman(number - 900)
        return roman(500) + roman(number - 500)
    elif 1000 <= number <= 5000:
        return roman(1000) + roman(number - 1000)
    else:
        raise ValueError('does not support numbers over 5000')


assert roman(1) == 'I'
assert roman(2) == 'II'
assert roman(3) == 'III'
assert roman(4) == 'IV'
assert roman(5) == 'V'
assert roman(6) == 'VI'
assert roman(7) == 'VII'
assert roman(8) == 'VIII'
assert roman(9) == 'IX'
# for i in range(1, 10):
#     print i, roman(i)

assert roman(10) == 'X'
assert roman(20) == 'XX'
assert roman(30) == 'XXX'
assert roman(40) == 'XL'
assert roman(50) == 'L'
assert roman(60) == 'LX'
assert roman(70) == 'LXX'
assert roman(80) == 'LXXX'
assert roman(90) == 'XC'
# print
# for i in range(10, 100, 10):
#     print i, roman(i)
assert roman(100) == 'C'
assert roman(200) == 'CC'
assert roman(300) == 'CCC'
assert roman(400) == 'CD'
assert roman(500) == 'D'
assert roman(600) == 'DC'
assert roman(700) == 'DCC'
assert roman(800) == 'DCCC'
assert roman(900) == 'CM'
assert roman(1000) == 'M'
# print
# for i in range(100, 1000+1, 100):
#     print i, roman(i)
assert roman(49) == 'XLIX'
assert roman(606) == 'DCVI'
assert roman(1606) == 'MDCVI'
assert roman(999) == 'CMXCIX'
assert roman(4999) == 'MMMMCMXCIX'
# print
# for i in [ 49, 606, 999, 1606, 4999 ]:
#     print i, roman(i)

def denary(roman):
    tmp = roman
    tmp = roman.replace('IV', '4')
    tmp = roman.replace('XL', '40')
    tmp = roman.replace('CD', '400')

    tmp = roman.replace('IX', '9')
    tmp = roman.replace('XC', '90')
    tmp = roman.replace('CM', '900')
    thousands = roman.count('M')
    five_hundreds = roman.count('D')
    hundreds = roman.count('C')
    tens = roman.count('X')
    tmp = roman.replace(thousands * THOUSAND, str(thousands))
    tmp = roman.replace(five_hundreds * FIVE_HUNDRED, str(five_hundreds))
    tmp = roman.replace(hundreds * HUNDRED, str(hundreds))
    tmp = roman.replace(tens * TEN, str(tens))
    tmp = roman.replace(FIVE + (3*ONE), 8)
    tmp = roman.replace(FIVE + (2*ONE), 7)
    tmp = roman.replace(FIVE + ONE, 6)
    tmp = roman.replace(FIVE, 5)

    ones = roman.count(ONE)
    tmp = roman.replace(ones * ONE, str(ones))

    return ''.join(list(tmp))
print denary('MMMMCMXCIX')
