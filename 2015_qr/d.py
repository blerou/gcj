import sys


def read_input(s):
    data = filter(len, s.replace("\n", " ").split(" "))
    data = map(int, data)
    result = []
    for _ in range(data.pop(0)):
        x, r, c = data[:3]
        data = data[3:]
        result.append((x, r, c))
    return result

dims = {1: [(1,1)],
        2: [(1,2)],
        3: [(1,3), (2,2)],
        4: [(1,4), (2,3), (2,2)]}

def solve(c):
    x, r, c = c
    print x, r, c
    if r * c % x != 0:
        return "RICHARD"
    for dim in dims[x]:
        i, j = dim
        print i, "x", j
        if min(r, c) < min(i, j):
            return "RICHARDmin"
        if max(r, c) < max(i, j):
            return "RICHARDmax"
        if r < i and c >= j or r >= i and c < j:
            return "RICHARDri"
        if r < j and c >= i or r >= j and c < i:
            return "RICHARDrj"

    return "GABRIEL"


if __name__ == "__main__":
    cases = read_input(sys.stdin.read())
    for i in range(len(cases)):
        print "Case #%d: %s" % (i + 1, solve(cases[i]))
