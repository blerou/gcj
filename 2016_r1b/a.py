import sys
from collections import defaultdict

def read_input():
    data = sys.stdin.read().split()
    for _ in xrange(int(data.pop(0))):
        n = data.pop(0)
        yield n

DIGITS = [("SIX", 6), ("ZERO", 0), ("TWO", 2), ("FOUR", 4), ("EIGHT", 8), ("ONE", 1), ("THREE", 3), ("FIVE", 5), ("SEVEN", 7), ("NINE", 9)]

DEBUG = False

def make_lcd(s):
    ss = defaultdict(int)
    for i in s:
        ss[i] += 1
    return ss

def contains(a, b):
    for k, v in b.iteritems():
        if a[k] < v:
            return False
    return True

def empty(lcd):
    for k, v in lcd.iteritems():
        if v > 0:
            return False
    return True

def solve(s):
    n = []
    ss = make_lcd(s)
    if DEBUG: print "ss: ", ss
    for ds, dn in DIGITS:
        d = make_lcd(ds)
        while contains(ss, d):
            n.append(dn)
            for k,v in d.iteritems():
                ss[k] -= v
            if DEBUG: print dn, " / ", ss
    if DEBUG: print n
    if not empty(ss): return "SZAR: %s" % ss
    else: return "".join(map(str, sorted(n)))


if __name__ == "__main__":
    i = 1
    for c in read_input():
        print "Case #%d: %s" % (i, solve(c))
        i += 1
