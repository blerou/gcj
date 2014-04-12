import sys

def read_input(s):
    data = map(float, filter(len, s.replace("\n", " ").split(" ")))
    result = []
    for _ in range(int(data.pop(0))):
        c, f, x = data[0:3]
        data = data[3:]
        result.append((c,f,x))
    return result

def solve(c):
    c, f, x = c
    rate, extra_time = 2, 0
    finish_at = extra_time + x / rate
    extra_time += c / rate
    rate += f
    next_at = extra_time + x / rate
    while next_at < finish_at:
        finish_at = next_at
        extra_time += c / rate
        rate += f
        next_at = extra_time + x / rate
    return finish_at

if __name__ == "__main__":
    cases = read_input(sys.stdin.read())
    for idx, c in map(lambda c, i: (i, c), cases, range(1, len(cases)+1)):
        print "Case #%d: %1.7f" % (idx, solve(c))
