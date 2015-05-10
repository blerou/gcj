import sys

def read_input():
    data = sys.stdin.read().split()
    for _ in xrange(int(data.pop(0))):
        r = int(data.pop(0))
        c = int(data.pop(0))
        w = int(data.pop(0))
        yield r, c, w

def solve(data):
    r, c, w = data
    if c == w:
        return w
    else:
        result = c / w + w - 1
        if c % w != 0:
            result += 1
        return result

if __name__ == "__main__":
    i = 1
    for c in read_input():
        print "Case #%d: %s" % (i, solve(c))
        i += 1
