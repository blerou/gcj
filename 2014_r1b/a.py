import sys
import itertools

def read_input():
    s = sys.stdin.read()
    data = filter(len, s.replace("\n", " ").split(" "))
    T = int(data.pop(0))
    cases = []
    for _ in xrange(T):
        N = int(data.pop(0))
        cases.append(data[0:N])
        data = data[N:]
    return cases

def norm_pairs(pairs):
    return [(ch, len(list(g))) for ch, g in pairs]

def chars(pairs):
    return [ch for ch, _ in pairs]

def lens(pairs):
    return [l for _, l in pairs]

def min_steps(len_list):
    steps = 0
    for i in xrange(len(len_list[0])):
        i_lens = [l[i] for l in len_list]
        best = sys.maxint
        for l in xrange(min(i_lens), max(i_lens)+1):
            x = sum([abs(l - il) for il in i_lens])
            if x < best: best = x
        steps += best
    return steps

def solve(c):
    sol = [itertools.groupby(pairs) for pairs in c]
    sol = [norm_pairs(pairs) for pairs in sol]
    char_list = [chars(pairs) for pairs in sol]
    if all([char_list[0] == chs for chs in char_list]):
        return min_steps(map(lens, sol))
    else:
        return "Fegla Won"

if __name__ == "__main__":
    cases = read_input()
    idx = 1
    for c in cases:
        print "Case #%d: %s" % (idx, solve(c))
        idx += 1
