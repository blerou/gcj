import sys
import itertools
import math
import time

def read_input():
    s = sys.stdin.read()
    data = filter(len, s.replace("\n", " ").split(" "))
    T = int(data.pop(0))
    for _ in xrange(T):
        N = int(data.pop(0))
        yield data[0:N]
        data = data[N:]

def shrink_chars(s): return [ch for ch, _ in itertools.groupby(s)]

def test_shrink_chars():
    s = [1, 1, 2, 2, 3]
    assert len(shrink_chars(s)) == 3
    assert 1 in shrink_chars(s)
    assert 2 in shrink_chars(s)
    assert 3 in shrink_chars(s)

def shrink_conseq_chars(string_list):
    return [shrink_chars(s) for s in string_list]


def has_no_separated_inner_char(char_list):
    inner_chars = list(itertools.chain(*[chs[1:-1] for chs in char_list]))
    for ch in inner_chars:
        if sum([int(ch1 == ch) for chs in char_list for ch1 in chs]) > 1:
            return False
    return True

def test_has_no_separated_inner_char():
    cl = [[1, 2, 3]]
    assert has_no_separated_inner_char(cl)
    cl = [[1, 2, 3], [2]]
    assert not has_no_separated_inner_char(cl)

def partition_tuples(chars_list):
    tuples = []
    singles = []
    for chs in chars_list:
        if len(chs) == 1:
            singles.append(chs)
        else:
            tuples.append(chs)
    return tuples, singles

def test_partition_tuples():
    def assert_tuples(tuples, singles, inp):
        t, s = partition_tuples(inp)
        assert t == tuples
        assert s == singles
    chs = [['a', 'b'], ['b', 'c']]
    assert_tuples(chs, [], chs)
    singles = [['a'], ['a']]
    assert_tuples([], singles, singles)
    assert_tuples(chs, singles, chs + singles)


def single_combination_cnt(singles):
    cnt = 1
    for _, g in itertools.groupby(singles):
        cnt *= math.factorial(len(list(g)))
    return cnt

def test_single_combination_cnt():
    s = ['a', 'b']
    assert 1 == single_combination_cnt(map(list, s))
    s = ['a', 'a', 'b']
    assert 2 == single_combination_cnt(map(list, s))
    s = ['a', 'a', 'b', 'b']
    assert 4 == single_combination_cnt(map(list, s))
    s = ['a', 'a', 'a']
    assert 6 == single_combination_cnt(map(list, s))


def get_connecting(pairs, pair):
    a0, b0 = pair
    return [(a1, b1) for a1, b1 in pairs if b0 == a1]


def remaining_pairs(pairs, i):
    return pairs[0:i]+pairs[i+1:]


def pair_combination_cnt(pairs, singles):
    all_items = reduce(lambda aggr, p: aggr | p, [set(p) for p in pairs], set())
    result = sum([1 for single in set([it[0] for it in singles]) if single not in all_items])
    begins = dict()
    ends = dict()
    for it in all_items:
        beg = [b for a, b in pairs if a == it]
        if len(beg) > 0:
            begins[it] = beg[0]
        en = [a for a, b in pairs if b == it]
        if len(en) > 0:
            ends[it] = en[0]

    return math.factorial(result + calculate_permutation(all_items, begins, ends))

def calculate_permutation(all_items, begins, ends):
    # print all_items
    # print begins
    # print ends
    used = set()
    result = 0
    while all_items - used:
        starting = ending = (all_items-used).pop()
        used.add(starting)
        while starting in begins:
            starting = begins[starting]
            used.add(starting)
        while ending in ends:
            ending = ends[ending]
            used.add(ending)
        result += 1
    return result




def test_pair_combination_cnt():
    p = [['a', 'b']]
    assert 1 == pair_combination_cnt(p)
    p = [['a', 'b'], ['c', 'd']]
    assert 2 == pair_combination_cnt(p)
    p = [['a', 'b'], ['c', 'd'], ['e', 'f']]
    assert 6 == pair_combination_cnt(p)
    p = [['a', 'b'], ['b', 'c']]
    assert 1 == pair_combination_cnt(p)
    p = [['b', 'c'], ['a', 'b']]
    assert 1 == pair_combination_cnt(p)
    p = [['a', 'b'], ['b', 'c'], ['d', 'e']]
    assert 2 == pair_combination_cnt(p)


def has_no_recurring_item_in_pair_positions(pairs):
    # print(pairs)
    fst = [a for a, _ in pairs]
    if len(fst) != len(set(fst)):
        # print "fst - ", fst, " / ", set(fst)
        return False
    snd = [b for _, b in pairs]
    if len(snd) != len(set(snd)):
        # print "snd - ", snd, " // ", set(snd)
        return False
    if any([(b, a) in pairs for a, b in pairs]):
        return False
    return True


def solve(string_list):
    chars_list = shrink_conseq_chars(string_list)
    if has_no_separated_inner_char(chars_list):
        tuples, singles = partition_tuples(chars_list)
        pairs = [(chs[0], chs[-1]) for chs in tuples]
        if has_no_recurring_item_in_pair_positions(pairs):
            # return pair_combination_cnt(pairs)
            return single_combination_cnt(singles) * pair_combination_cnt(pairs, singles)
    return 0

if __name__ == "__main__":
    cases = read_input()
    idx = 1
    for c in cases:
        print "Case #%d: %s" % (idx, solve(c))
        idx += 1
