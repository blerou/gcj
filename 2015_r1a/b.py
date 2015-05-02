import sys
from fractions import gcd

def read_input():
    data = sys.stdin.read().split()
    for _ in xrange(int(data.pop(0))):
        b = int(data.pop(0))
        n = int(data.pop(0))
        m = map(int, data[:b])
        yield n, m
        data = data[b:]

def lcm(a, b):
    if a > b: return a / gcd(a, b) * b
    else: return b / gcd(a, b) * a

def solve(c):
    n, m = c
    # print n, m
    t_period = reduce(lcm, m)
    customer_per_period = 0
    for t_barber in m:
        customer_per_period += t_period / t_barber
    barbers = [(0, b) for b in range(len(m))]
    n = n % customer_per_period
    # print "per period: %d, new n: %d" % (customer_per_period, n)
    if n == 0:
        n = customer_per_period
    for _ in xrange(n-1):
        # print barbers
        t, b = barbers.pop(0)
        # print "t: %d, b: %d" % (t, b)
        barbers.append((t + m[b], b))
        barbers.sort()
    _, b = barbers.pop(0)
    return b+1

if __name__ == "__main__":
    i = 1
    for c in read_input():
        print "Case #%d: %s" % (i, solve(c))
        i += 1
