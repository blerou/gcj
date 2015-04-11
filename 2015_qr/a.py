import sys


def read_input(s):
    data = filter(len, s.replace("\n", " ").split(" "))
    result = []
    for _ in range(int(data.pop(0))):
        smax = int(data.pop(0))
        ss = map(int, data.pop(0))[:smax + 1]
        result.append(ss)
    return result


def solve(ss):
    current_s = 0
    clapping = 0
    req_friends = 0
    while current_s < len(ss):
        clapping += ss[current_s]
        current_s += 1
        if clapping <= current_s:
            req_friends += current_s - clapping
            clapping = current_s
    return req_friends


if __name__ == "__main__":
    cases = read_input(sys.stdin.read())
    for i in range(len(cases)):
        print "Case #%d: %s" % (i + 1, solve(cases[i]))
