import sys

def read_input():
    s = sys.stdin.read()
    data = filter(len, s.replace("\n", " ").split(" "))
    T = int(data.pop(0))
    for _ in xrange(T):
        P, Q = data.pop(0).split("/")
        yield int(P), int(Q)


def solution(P, Q):
    g = 0
    while Q % 2 == 0 and P < Q and g < 40:
        g += 1
        Q /= 2
        # print "P: %d, Q: %d, g: %d" % (P, Q, g)
    if P == Q and Q % 2 == 1:
        return g
    if P >= Q and Q % 2 == 0:
        return g
    return -1


def solve(c):
    P, Q = c
    # print "P: %d, Q: %d" % (P, Q)
    if P <= Q/2:
        s = solution(P, Q)
    else:
        s = solution(P, Q)
        if Q % 2 == 0:
            check = solution(P-Q/2, Q)
        else:
            check = -1
        # print "P: %d, Q: %d, check: %d" % (P, Q, check)
        if check == -1:
            return "impossible"
    if s == -1:
        return "impossible"
    else:
        return s

if __name__ == "__main__":
    cases = read_input()
    idx = 1
    for c in cases:
        print "Case #%d: %s" % (idx, solve(c))
        idx += 1
