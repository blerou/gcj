import sys

def read_input():
    data = sys.stdin.read.split()
    for _ in xrange(int(data.pop(0))):

        yield

def solve(c):
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
    i = 1
    for c in read_input():
        print "Case #%d: %s" % (i, solve(c))
        i += 1
