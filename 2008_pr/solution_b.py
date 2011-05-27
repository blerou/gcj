import sys

NORTH = 1
SOUTH = 2
WEST = 4
EAST = 8


def fgets(f):
  return f.readline().rstrip("\n")

def move(pos, dir):
  return (pos[0]+dir[0], pos[1]+dir[1])

def cmp_maze(a, b):
  pos_a, pos_b = a[0], b[0]
  r = cmp(pos_a[0], pos_b[0])
  if r == 0:
    r = cmp(pos_a[1], pos_b[1])
  return r

def build_maze(maze_desc, pos=(0, 0), dir=SOUTH):
  dirs = { NORTH: (0, 1), SOUTH: (0, -1), WEST: (-1, 0), EAST: (1, 0) }
  ops = { NORTH: SOUTH, SOUTH: NORTH, WEST: EAST, EAST: WEST }
  left = { NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH }
  right = { NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH }
  maze = {}
  for char in maze_desc:
    if char == 'W':
      pos = move(pos, dirs[dir])
      if pos not in maze.keys():
        maze[pos] = 0
      maze[pos] = maze[pos] | ops[dir]
    elif char == 'R':
      dir = right[dir]
    elif char == 'L':
      dir = left[dir]
  return (maze, pos, ops[dir])

def solve_case(to_exit, from_exit):
  t, pos, dir = build_maze(to_exit)
  f, pos, dir = build_maze(from_exit, pos, dir)
  maze = {}
  for pos, desc in t.iteritems():
    if pos in f.keys():
      maze[pos] = desc | f[pos]
  maze = maze.items()
  print maze
  maze.sort(cmp_maze)
  return maze
  

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print "Gimme the input file..."
    sys.exit()
  fin = open(sys.argv[1], 'r')
  fout = open(sys.argv[1]+'.out', 'w')
  for case_index in range(int(fgets(fin))):
    to_exit, from_exit = fgets(fin).split(' ', 3)
    r = solve_case(to_exit, from_exit)
    print r
    continue
    print "Case #%d: %s" % (case_index+1, r)
    fout.write("Case #%d: %s\n" % (case_index+1, r))
  fin.close()
  fout.close()
