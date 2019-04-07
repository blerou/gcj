import math
import sys

def solve(n, ct):
    idx = len(ct)-1
    m = ct[idx]
    
    if m % 2 == 0:
        a = 2
    else:
        for a in range(3, math.ceil(math.sqrt(m))+1, 2):
            if m % a == 0:
                break
    b = int(m / a)

    ctp = [None for _ in ct]
    ctp[idx] = (a, b)
    for i in range(idx-1, -1, -1):
        a, b = ctp[i+1]
        if ct[i] % b == 0:
            c = b
        else:
            c = a
        ctp[i] = (c, int(ct[i]/c))

    ptn = []
    a, b = ctp[0]
    if a in ctp[1]:
        ptn.append(b)
        c = a
    else:
        ptn.append(a)
        c = b
    for i in range(1, len(ctp)):
        a, b = ctp[i]
        ptn.append(c)
        if c == a:
            c = b
        else:
            c = a
    ptn.append(c)

    ps = sorted(set(ptn))
    pt = ""
    for i in range(len(ptn)):
        pt += chr(ps.index(ptn[i])+65)

    return pt

data = sys.stdin.read().split()
for i in range(1, int(data.pop(0))+1):
    n = int(data.pop(0))
    l = int(data.pop(0))
    ct = [int(data.pop(0)) for _ in range(l)]
    pt = solve(n, ct)
    print("Case #%d: %s" % (i, pt))
