import sys
import re

def fgets(f):
  return f.readline().rstrip("\n")


def solve_case(p, words):
  pattern = p.replace('(', '[').replace(')', ']')
  
  count = 0
  for word in words:
    if re.match(pattern, word):
      count += 1
  return count

if __name__ == '__main__':
  fin = open(sys.argv[1], 'r')
  fout = open(sys.argv[1]+'.out', 'w')
  
  L, D, N = map(int, re.findall('\d+', fgets(fin)))
  
  words = []
  for i in range(D):
    words.append(fgets(fin))
  
  for case_index in range(N):
    m = solve_case(fgets(fin), words)
    r = "Case #%d: %d" % (case_index + 1, m)
    print r
    fout.write(r + "\n")
    
  fin.close()
  fout.close()
