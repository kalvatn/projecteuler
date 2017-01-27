import math
from fractions import Fraction


# print math.sqrt(2)
def nest(n, f=Fraction(1, 2)):
    # print n, f
    if n <= 1:
        return 1 + f
    return nest(n-1, Fraction(1, 2 + f))

# nest(1000) # stack explodes

f = Fraction(1, 2)
count = 0
for i in range(1, 1000+1):
    f2 = 1 + f
    n = f2.numerator
    d = f2.denominator
    if len(str(n)) > len(str(d)):
        count += 1
        # print i, 1 + f

    f = Fraction(1, 2 + f)
# print 1 + f
print count
