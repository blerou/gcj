import sys

def solve(q, ps):

data = sys.stdin.read().split()
for i in range(int(data.pop(0))):
    p = int(data.pop(0))
    q = int(data.pop(0))
    ps = [(int(data.pop(0)), int(data.pop(0)), data.pop(0)) for _ in range(p)]
    x, y = solve(q, ps)
    print("Case #%d: %d %d" % (i+1, x, y))
