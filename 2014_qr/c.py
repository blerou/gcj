import sys

def read_input(s):
    data = map(int, filter(len, s.replace("\n", " ").split(" ")))
    result = []
    for _ in range(data.pop(0)):
        r, c, m = data[0:3]
        data = data[3:]
        result.append((r,c,m))
    return result

def mine_block(s, dim):
    x, y = s
    r, c = dim
    return [(x+i, y+j) for i in range(r) for j in range(c)]

def neighbours(cell):
    x, y = cell
    return [(x + i, y + j) for i in [-1, 0, 1] for j in [-1, 0, 1] if i != 0 or j != 0]

def test_neighbours():
    assert [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)] == neighbours((2,2))

def has_mine_neighbour(cell, mines):
    return len(set(mines) & set(neighbours(cell))) > 0

def extract_cells(r, c, mines):
    digits, free = [], []
    cells = [(i, j) for i in range(1, r+1) for j in range(1, c+1)]
    for cell in set(cells) - set(mines):
        if has_mine_neighbour(cell, mines):
            digits.append(cell)
        else:
            free.append(cell)
    return digits, free

def digits_with_no_free_neighbours(digits, free):
    with_neighbours = [cell for cell in digits if len(set(neighbours(cell)) & set(free)) > 0]
    return set(digits) - set(with_neighbours)

def solvable(r, c, mines):
    digits, free = extract_cells(r, c, mines)
    all_digits_is_one = len(free) == 0 and len(digits) == 1
    if all_digits_is_one:
        return True
    return len(digits_with_no_free_neighbours(digits, free)) == 0

def solve(c):
    r,c,m = c
    dim_r, dim_c = r, c
    s = (1, 1)
    mines = []
    while m >= min(r, c):
        if r < c:
            m = m - r
            mines.extend(mine_block(s, (r, 1)))
            x, y = s
            s = (x, y + 1)
            c = c - 1
        else:
            m = m - c
            mines.extend(mine_block(s, (1, c)))
            x, y = s
            s = (x + 1, y)
            r = r - 1
    if m > 0:
        if r > c and r - 2 >= m:
            mines.extend(mine_block(s, (m, 1)))
        elif c > r and c - 2 >= m:
            mines.extend(mine_block(s, (1, m)))
        else:
            x, y = s
            places = [(x+i, y+j) for i in range(r) for j in range(c)]
            fillup = []
            for a in range(50):
                fillup.extend([(i,j) for i in range(a) for j in range(a) if i+j == a and (i,j) in places])
            best_fill_places = fillup[0:m]
            mines.extend(best_fill_places)



    # print "mines", mines
    # print "digits", digits
    # print "free", free
    # print non_free_neighbour_digit
    # print "================\n%s\n================" % render(mines, dim_r, dim_c)

    if solvable(dim_r, dim_c, mines):
        return render(mines, dim_r, dim_c)
    else:
        # print "================\n%s\n================" % render(mines, dim_r, dim_c)
        return "Impossible"

def render(mines, r, c):
    s = ""
    for x in range(1, r+1):
        for y in range(1, c+1):
            if (x, y) in mines:
                s += "*"
            elif x == r and y == c:
                s += "c"
            else:
                s += "."
        s += "\n"
    return s.rstrip("\n")


if __name__ == "__main__":
    cases = read_input(sys.stdin.read())
    for idx, c in map(lambda c, i: (i, c), cases, range(1, len(cases)+1)):
        print "Case #%d:\n%s" % (idx, solve(c))
