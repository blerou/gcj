import sys

def solve(n):
    a, b = "", ""
    for c in str(n):
        if c == "4":
            a += "3"
            b += "1"
        else:
            a += c
            b += "0"
    return a, b  

data = sys.stdin.read().split()
for i in range(int(data.pop(0))):
    n = int(data.pop(0))
    a, b = solve(n)
    print("Case #%d: %s %s" % (i+1, a, b))
