import sys
import copy

def read_input():
    data = sys.stdin.read().split()
    for _ in xrange(int(data.pop(0))):
        c = int(data.pop(0))
        d = int(data.pop(0))
        v = int(data.pop(0))
        D = set(map(int, data[:d]))
        yield c, D, v
        data = data[d:]

def can_purchase(v, D):
    D = copy.copy(D)
    while v > 0 and len(D) > 0:
        nxt = 0
        for d in D:
            if nxt < d <= v:
                nxt = d
        # print "next", nxt
        if nxt == 0:
            return False
        v -= nxt
        D.remove(nxt)
        # print "remaining", v, "Ds", D
    return v == 0


def solve(data):
    # print data
    # in small c = 1 so ignore it
    c, D, v = data
    result = 0
    for i in xrange(v):
        value = i+1
        if not can_purchase(value, D):
            result += 1
            D.add(value)
        # print i, ". ", D
    return result

if __name__ == "__main__":
    i = 1
    for c in read_input():
        print "Case #%d: %s" % (i, solve(c))
        i += 1
