import sys


T = {"1": {"1": ("1", True),
           "i": ("i", True),
           "j": ("j", True),
           "k": ("k", True)},
     "i": {"1": ("i", True),
           "i": ("1", False),
           "j": ("k", False),
           "k": ("j", True)},
     "j": {"1": ("j", True),
           "i": ("k", True),
           "j": ("1", False),
           "k": ("i", False)},
     "k": {"1": ("k", True),
           "i": ("j", False),
           "j": ("i", True),
           "k": ("1", False)}}


def read_input(s):
    data = filter(len, s.replace("\n", " ").split(" "))
    result = []
    for _ in range(int(data.pop(0))):
        l = int(data.pop(0))
        x = int(data.pop(0))
        s = map(lambda a: (a, True), data.pop(0)[:l])
        result.append((s, x))
    return result


def mul(a, b):
    c1, s1 = a
    c2, s2 = b
    r, s3 = T[c2][c1]
    return r, s1 ^ s2 ^ s3


def unit():
    return "1", True


def calc(exp, pos, val, term, act_term, term_cnt, tries):
    while val != (exp, True) and pos < len(term):
        val = mul(val, term[pos])
        pos += 1
    if val != (exp, True):
        if tries:
            return calc(exp, 0, val, term, act_term + 1, term_cnt, tries - 1)
        else:
            raise Exception()
    if pos == len(term):
        pos = 0
        act_term += 1
    if act_term > term_cnt:
        raise Exception()
    return pos, act_term


def calc_term(term):
    val = unit()
    for c in term:
        val = mul(val, c)
    return val


def solve(c):
    try:
        term, term_cnt = c
        act_term = 1
        term_val = calc_term(term)
        tries = 32 / len(term) + 1 if len(term) < 32 else 1

        pos, act_term = calc("i", 0, unit(), term, act_term, term_cnt, tries)
        pos, act_term = calc("j", pos, unit(), term, act_term, term_cnt, tries)

        kval = unit()
        while pos < len(term):
            kval = mul(kval, term[pos])
            pos += 1
        for _ in range((term_cnt - act_term) % 4):
            kval = mul(kval, term_val)
        if kval != ("k", True):
            return "NO"
        return "YES"
    except:
        return "NO"


if __name__ == "__main__":
    cases = read_input(sys.stdin.read())
    for i in range(len(cases)):
        print "Case #%d: %s" % (i + 1, solve(cases[i]))
