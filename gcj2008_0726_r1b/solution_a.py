import sys
import re

def get_tree_pos(n, A, B, C, D, x0, y0, M):
  X, Y = x0, y0
  points = [(X, Y)]
  for i in range(n - 1):
    X = (A * X + B) % M
    Y = (C * Y + D) % M
    points.append((X, Y))
  return points

def solve_case(trees):
  pass

if __name__ == '__main__':
  fin = open(sys.argv[1], 'r')
  for case_index in range(int(fin.readline())):
    data = map(int, re.findall('\d+', fin.readline()))
    trees = get_tree_pos(*data)
    r = solve_case(trees)
  
  fin.close()

