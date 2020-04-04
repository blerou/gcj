import sys

def solve(s):
    r = ""
    p = 0
    for c in s:
        n = int(c)
        if n > p:
            r += "("*(n-p)
            r += c
        elif n < p:
            r += ")"*(p-n)
            r += c
        else:
            r += c
        p = n
    if p > 0:
        r += ")"*p
    return r

t = int(sys.stdin.readline())
for i in range(1, t+1):
    s = sys.stdin.readline().rstrip()
    print("Case #%d: %s" % (i, solve(s)))

