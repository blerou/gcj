import math
import sys

exp = int(sys.argv[1])
n = pow(10, exp)

ps = [2]
for i in range(3, n, 2):
    sqrti = math.sqrt(i)
    match = False
    for p in ps:
        if p > sqrti:
            break
        if i % p == 0:
            match = True
            break
    if match:
        continue
    ps.append(i)

print(ps)
