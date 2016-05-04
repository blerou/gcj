import sys
from collections import defaultdict

def read_input():
    data = sys.stdin.read().split()
    for _ in xrange(int(data.pop(0))):
        c = data.pop(0)
        j = data.pop(0)
        yield c,j

DEBUG = False

def r(v):
    for i in [0, max(0, v-1), v, min(v+1, 9), 9]:
        if i >= 0 and i <= 9:
            yield i

def d(v):
    return v >= 0

def s(v):
    return "".join(map(str, v))

def solve(p):
    c, j = p
    c = list(c)
    j = list(j)
    for i in range(len(c)):
        if c[i] == "?":
            c[i] = -1
        else:
            c[i] = int(c[i])
        if j[i] == "?":
            j[i] = -1
        else:
            j[i] = int(j[i])
    # pad leading zeros
    i = 0
    while i < len(c) and c[i] < 0 and j[i] < 0:
        c[i] = 0
        j[i] = 0
        i += 1
    # start
    q = [(c,j,0)]
    result = ("0", "999999999999999999", 999999999999999999)
    while q:
        c, j, i = q.pop(0)
        if i == len(c):
            c1 = int(s(c))
            j1 = int(s(j))
            a = abs(c1 - j1)
            if a < result[2]:
                result = (c,j,a)
            elif a == result[2] and c1 < int(s(result[0])):
                result = (c,j,a)
            elif a == result[2] and c1 == int(s(result[0])) and j1 < int(s(result[1])):
                result = (c,j,a)
        elif d(c[i]) and d(j[i]):
            q.append((c,j,i+1))
        elif d(c[i]):
            for l in r(c[i]):
                x = j[:]
                x[i] = l
                q.append((c,x,i+1))
        elif d(j[i]):
            for l in r(j[i]):
                x = c[:]
                x[i] = l
                q.append((x,j,i+1))
        else:
            for k in [0,1,9]:
                for l in [0,1,9]:
                    x = c[:]
                    x[i] = k
                    y = j[:]
                    y[i] = l
                    q.append((x,y,i+1))
    c,j,a = result
    return "%s %s" % (s(c), s(j))
    

if __name__ == "__main__":
    i = 1
    for c in read_input():
        print "Case #%d: %s" % (i, solve(c))
        i += 1
