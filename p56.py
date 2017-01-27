
highest = 0
for a in range(1, 100):
    for b in range(1, 100):
        s = sum(map(int, list(str(a**b))))
        if s > highest:
            highest = s
            # print a, b, s
print highest
