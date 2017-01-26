from lib import euler
from lib.euler import binomial_coefficient as bc


assert bc(5, 3) == 10
assert bc(23, 10) == 1144066
values = []

for n in range(1, 100+1):
    # print n
    for r in range(1, n+1):
        ncr = bc(n, r)
        if ncr > 10**6:
            values.append(ncr)
            # print n, r, ncr

print len(values)

