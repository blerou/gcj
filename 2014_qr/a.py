
import sys

def extract_row(data):
    chosen = data.pop(0)
    row = data[(chosen-1)*4:chosen*4]
    return row, data[16:]

def test_extract_row():
    base = [2]
    base.extend(range(1, 17))
    base.append(3)
    assert ([5,6,7,8], [3]) == extract_row(base)



def read_input(s):
    data = map(int, filter(len, s.replace("\n", " ").split(" ")))
    result = []
    for _ in range(data.pop(0)):
        first, data = extract_row(data)
        second, data = extract_row(data)
        result.append((first, second))
    return result



def solve(c):
    first, second = c
    possible_solutins = set(first) & set(second)
    if len(possible_solutins) == 1:
        return list(possible_solutins)[0]
    elif len(possible_solutins) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


def test_solve():
    assert 3 == solve(([1, 2, 3, 4], [5, 6, 3, 7]))



if __name__ == "__main__":
    cases = read_input(sys.stdin.read())
    for idx, c in map(lambda c, i: (i, c), cases, range(1, len(cases)+1)):
        print "Case #%d: %s" % (idx, solve(c))
        
