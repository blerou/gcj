import sys
import re

def fgets(f):
  return f.readline().rstrip("\n")

def solve_case():
  pass

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print "Gimme the input file..."
    sys.exit()
  
  fin = open(sys.argv[1], 'r')
  fout = open(sys.argv[1]+'.out', 'w')
  
  for case_index in range(int(fgets(fin))):
    r = solve_case()
    r = "Case #%d: %s" % (case_index+1, r)
    print r
    fout.write("%s\n" % (r,))
  
  fin.close()
  fout.close()

