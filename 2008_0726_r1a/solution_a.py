import sys
import re

def fgets(f):
  return f.readline().rstrip("\n")

def read_case(f):
  l = int(fgets(f))
  v1 = map(int, re.findall('-?\d+', fgets(f)))
  v2 = map(int, re.findall('-?\d+', fgets(f)))
  return (l, (v1, v2))

def solve_case(l, v1, v2):
  v1.sort()
  v1.reverse()
  v2.sort()
  v = [v1[i] * v2[i] for i in range(l)]
  return sum(v)

fin = open(sys.argv[1], 'r')
for case_index in range(1, int(fgets(fin)) + 1):
  l, (v1, v2) = read_case(fin)
  r = solve_case(l, v1, v2)
  print "Case #%d: %d" % (case_index, r)
fin.close()
