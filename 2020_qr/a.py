import sys

def solve(n, m):
    t = 0
    r = 0
    c = 0
    for i in range(n):
        t += m[i][i]
        if len(set(m[i])) != n:
            r += 1
        if len(set([m[j][i] for j in range(n)])) != n:
            c += 1
    return "%d %d %d" % (t, r, c) 

t = sys.stdin.readline()
for i in range(1, int(t)+1):
    n = int(sys.stdin.readline())
    m = []
    for _ in range(n):
        row = sys.stdin.readline().split(" ")
        m.append([int(x) for x in row])
    print("Case #%d: %s" % (i, solve(n, m)))
