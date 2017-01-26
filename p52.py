#!/usr/bin/env python

for i in xrange(1, 10**6):
    digits = list(sorted(str(i)))
    same = True
    for x in range(2, 7):
        if not list(sorted(str(i*x))) == digits:
            same = False
    if same:
        print i

