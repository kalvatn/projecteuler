
from lib.euler import is_palindrome

def is_lychrel(n, it=1):
    rn = int(''.join(reversed(str(n))))
    s = n + rn
    # print n, rn, s, it
    if is_palindrome(s):
        return False
    if it >= 50:
        return True
    return is_lychrel(s, it=it+1)

assert not is_lychrel(349)

# for i in range(1, 10000+1):
count = 0
for i in range(1, 10000):
    if is_lychrel(i, it=1):
        count += 1
        # print i
print count


