import sys
import re

TEXT = list('welcome to code jam')

def fgets(f):
  return f.readline().rstrip("\n")

def solve(subject, pos, count):
  if pos == len(TEXT):
    count += 1
    return count % 1000
  
  char = TEXT[pos]
  
  p = subject.find(char, 0)
  while -1 != p:
    count = solve(subject[p+1:], pos+1, count)
    p = subject.find(char, p+1)
  
  return count

def solve_case(subject):
  return solve(subject, 0, 0)

if __name__ == '__main__':
  fin = open(sys.argv[1], 'r')
  fout = open(sys.argv[1]+'.out', 'w')
  
  for case_index in range(int(fgets(fin))):
    count = solve_case(fgets(fin))
    r = "Case #%d: %04d" % (case_index + 1, count)
    print r
    fout.write(r + "\n")
    
  fin.close()
  fout.close()
