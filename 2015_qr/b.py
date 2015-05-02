import sys


def read_input(s):
    data = filter(len, s.replace("\n", " ").split(" "))
    data = map(int, data)
    result = []
    for _ in range(data.pop(0)):
        d = data.pop(0)
        ps = dict()
        for p in data[:d]:
            ps[p] = ps.get(p, 0) + 1
        data = data[d:]
        result.append(ps)
    return result


def solve(ps):
    mins = 0
    sm = 1001
    while True:
        # print ps, "@", mins
        pmax = max(ps.keys())
        sm = min(sm, pmax + mins)
        pcnt = ps[pmax]
        small_half = pmax / 2
        large_half = pmax - small_half
        if pmax > 3 and mins < sm:
            if small_half not in ps:
                ps[small_half] = 0
            if large_half not in ps:
                ps[large_half] = 0
            ps[small_half] += pcnt
            ps[large_half] += pcnt
            del ps[pmax]
            mins += pcnt
        else:
            return sm


if __name__ == "__main__":
    cases = read_input(sys.stdin.read())
    for i in range(len(cases)):
        print "Case #%d: %s" % (i + 1, solve(cases[i]))
