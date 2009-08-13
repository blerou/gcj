import sys
import re

def fgets(f):
  return f.readline().rstrip("\n")

def cmp_pair(a, b):
  return cmp(len(a), len(b))

def cmp_flavor(a, b):
  return cmp(a[1], b[1])

def build_pairs(f, M):
  pairs = []
  for cust in range(M):
    cnt, p = map(int, re.findall('\d+', fgets(f)))
    r = [(p[i*2], p[i*2+1]) for i in range(cnt)]
    r.sort(cmp_flavor)
    pairs.append(r) 
  pairs.sort(cmp_pair)
  return pairs

def solve_case(fin):
  N, M = int(fgets(fin)), int(fgets(fin))
  pairs = build_pairs(fin, M)
  #print pairs
  mix = dict([(i, None) for i in range(1, N + 1)])
  for i in range(M):
    imp = True
    for flavor, malted in pairs[i]:
      if mix[flavor] == None or mix[flavor] == malted:
        mix[flavor] = malted
        imp = False
        break
    if imp:
      return "IMPOSSIBLE"
  for k, v in mix.iteritems():
    if v == None:
      mix[k] = 0
  return ' '.join('%d' % v for v in mix.values())

fin = open(sys.argv[1], 'r')
for case_index in range(1, int(fgets(fin)) + 1):
  r = solve_case(fin)
  print "Case #%d: %s" % (case_index, r)
  #print '====='
fin.close()
