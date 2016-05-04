import sys

def read_input():
    data = sys.stdin.read().split()
    for _ in xrange(int(data.pop(0))):
        yield tuple(map(int, data[:3]))
        data = data[3:]

def max_happy(r, c):
    happy_cnt = 0
    for i in xrange(r):
        for j in xrange(c):
            if (i + j) % 2 == 0:
                happy_cnt += 1
    return happy_cnt

def row_places(r, current_c):
    result = r / 2
    if r % 2 and current_c % 2 == 0:
        result += 1
    return result

def unhappy_for_cell_in(r, c, current_c):
    if current_c == c - 1:
        return 0
    if r > 1:
        return 3 if current_c % 2 else 2
    else:
        return current_c % 2

def last_place(r, current_c):
    return r > 1 and r % 2 == 1 and current_c % 2 == 0

def solve(c):
    r, c, n = c
    happy = max_happy(r, c)
    if happy >= n:
        return 0
    else:
        rem = n - happy
        unhappy = 0
        for current_c in xrange(c):
            rp = row_places(r, current_c)
            unhappy_cnt = unhappy_for_cell_in(r, c, current_c)
            if rem < rp:
                unhappy += rem * unhappy_cnt
                return unhappy
            else:
                unhappy += rp * unhappy_cnt
                if last_place(r, current_c):
                    unhappy -= 1
                rem -= rp

if __name__ == "__main__":
    i = 1
    for c in read_input():
        print "Case #%d: %s" % (i, solve(c))
        i += 1
