
from string import ascii_lowercase as alpha_lower
from string import ascii_uppercase as alpha_upper
from itertools import combinations_with_replacement as cr
from itertools import permutations
from lib.util import read_file
import time

print 'combos'

alphabet = alpha_lower + alpha_upper
print alphabet


cipher = []
for c in read_file('p59.txt')[0].split(','):
    cipher.append(int(c))

for c in alpha_lower:
    print c, ord(c)

for c in cr('b', 3):
    decrypted = ''
    for x in cipher:
        d = x
        for key in [ ord(cx) for cx in c ]:
            d = d ^ key
        print chr(d)
        if chr(d) not in alphabet:
            # print chr(d), 'not in alphabet'
            break
            decrypted += chr(d)





