import sys

def read_input():
    data = sys.stdin.read().split()
    for _ in xrange(int(data.pop(0))):
        c = int(data.pop(0))
        d = int(data.pop(0))
        v = int(data.pop(0))
        D = set(map(int, data[:d]))
        yield c, D, v
        data = data[d:]

def solve(data):
    # print data
    # in small c = 1 so ignore it
    c, D, v = data
    Ds = set(D)
    ds = {1}
    max_d = 1
    max_coin = max_d * c
    while True:
        while True:
            from_d = set([d for d in Ds if max_d < d <= max_coin])
            if len(from_d) == 0:
                break
            ds.update(from_d)
            Ds.difference_update(from_d)
            max_d = max(from_d)
            max_coin += sum(from_d) * c
        if v <= max_coin:
            break
        ds.add(max_coin+1)
        max_d = max_coin + 1
        max_coin += max_d * c
    return len(ds.difference(D))

if __name__ == "__main__":
    i = 1
    for c in read_input():
        print "Case #%d: %s" % (i, solve(c))
        i += 1
