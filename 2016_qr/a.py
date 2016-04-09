import sys

def read_input():
    data = sys.stdin.read().split()
    for _ in xrange(int(data.pop(0))):
        n = int(data.pop(0))
        yield n

def solve(n):
    if n == 0:
        return "INSOMNIA"
    else:
        digits = set(map(str, range(10)))
        for i in range(1,100):
            ne = n*i
            ds = set(str(ne))
            digits = digits - ds
            if len(digits) == 0:
                return ne


if __name__ == "__main__":
    i = 1
    for c in read_input():
        print "Case #%d: %s" % (i, solve(c))
        i += 1
