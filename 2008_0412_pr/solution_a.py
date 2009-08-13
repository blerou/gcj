import sys

def fgets(f):
  return f.readline().rstrip("\n")

def solve_case(num, src, trg):
  src_base = len(src)
  num10 = 0
  exp = 0
  for x in num[::-1]:
    num10 += pow(src_base, exp) * int(src.index(x))
    exp += 1
  
  trg_base = len(trg)
  r = ''
  while num10 / trg_base:
    r = '%s' % (trg[num10 % trg_base]) + r
    num10 /= trg_base
  r = '%s' % (trg[num10]) + r
  
  return r

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print "Gimme the input file..."
    sys.exit()
  fin = open(sys.argv[1], 'r')
  fout = open(sys.argv[1]+'.out', 'w')
  for case_index in range(int(fgets(fin))):
    num, src, trg = fgets(fin).split(' ', 3)
    r = solve_case(num, src, trg)
    print "Case #%d: %s" % (case_index+1, r)
    fout.write("Case #%d: %s\n" % (case_index+1, r))
  fin.close()
  fout.close()

