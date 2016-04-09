import sys

def read_input():
    data = sys.stdin.read().split()
    for _ in xrange(int(data.pop(0))):
        c = int(data.pop(0))
        i = int(data.pop(0))
        ps = map(int, data[0:i])
        data = data[i:]
        yield c, ps

# def a(c, ps, result):
#     pa = sorted(ps, key=lamba x: x[1])
#     p, g = pa.pop()
#     pb = filter(pa, lambda x: x[1] < g)
#     if len(pb) == 0:
#         return result
#     else:
#         return a(c-g, pb, result + [p])

def solve(data):
    c, ps = data
    for i, p1 in enumerate(ps):
        for j, p2 in enumerate(ps):
            if p1+p2 == c and i != j:
                return "%d %d" % (i+1, j+1)

if __name__ == "__main__":
    i = 1
    for c in read_input():
        print "Case #%d: %s" % (i, solve(c))
        i += 1
