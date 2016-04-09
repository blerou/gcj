import sys

def read_input():
    data = sys.stdin.read().split()
    for _ in xrange(int(data.pop(0))):
        s = data.pop(0)
        yield s

DEBUG = False

def solve(s):
    turns = 0
    n = len(s)
    i = 0
    i0 = 0
    if DEBUG: print "start", s
    while i < n:
        while i < n and s[i] == "-":
            i += 1
        if i != i0:
            turns += 1
        i0 = i
        if DEBUG: print "%s, i:%d, n:%d, turns:%d" % ("-", i, n, turns)
        while i < n and s[i] == "+":
            i += 1
        if i != i0 and i < n:
            turns += 1
        i0 = i
        if DEBUG: print "%s, i:%d, n:%d, turns:%d" % ("+", i, n, turns)
    return turns

if __name__ == "__main__":
    i = 1
    for c in read_input():
        print "Case #%d: %s" % (i, solve(c))
        i += 1
