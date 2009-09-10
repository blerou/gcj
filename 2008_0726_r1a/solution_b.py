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
  for _ in range(M):
    cnt = map(int, re.findall('\d+', fgets(f)))
    p, cnt = cnt[1:], cnt[0]
    r = [(p[i*2], p[i*2+1]) for i in range(cnt)]
    r.sort(cmp_flavor)
    pairs.append(r) 
  pairs.sort(cmp_pair)
  return pairs

def build_mix(N, M, pairs):
  mix = dict([(m, dict([(n+1, [True, True]) for n in range(N)])) for m in range(M)])
  cust_cnt = 0
  for customer in pairs:
    cmix = dict([(n+1, [False, False]) for n in range(N)])
    irrel = dict([(n+1, [True, True]) for n in range(N)])
    
    """gather personal preferences, irrelevant flavors-malts"""
    for flav, malt in customer:
      try:
        cmix[flav][malt] = True
        irrel[flav] = [False, False]
      except IndexError:
        print "%s: %s" % (flav, malt)
        print cmix
        print irrel
        return
    
    """finalize personal preferences"""
    for flav, m in irrel.iteritems():
      for malt in range(2):
        if m[malt]:
          cmix[flav][malt] = True
    
    """globalis preferenciak osszesitese"""
    for flav, m in cmix.iteritems():
      for malt in range(2):
        try:
          mix[cust_cnt][flav][malt] = cmix[flav][malt]
        except KeyError:
          print "%s / %s: %s" % (cust_cnt, flav, malt)
          print mix
          return
    
    cust_cnt += 1
  
  return mix

def build_choice(N, M, pairs, mix):
  """choose a shake person by person which match others preferences"""
  m = 0
  for customer in pairs:
    r = []
    for flav, malt in customer:
      r = [flav, malt]
      for n in range(1, N+1):
        r[1] = r[1] and mix[m][flav][malt]
        if not r[1]:
          break
      if not r[1]:
        break
    
    m += 1

def solve_case(fin):
  N, M = int(fgets(fin)), int(fgets(fin))
  
  pairs = build_pairs(fin, M)
  
  mix = build_mix(N, M, pairs)
  
  return build_choice(N, M, mix)
  
if __name__ == '__main__':
  fin = open(sys.argv[1], 'r')
  for case_index in range(1, int(fgets(fin)) + 1):
    r = solve_case(fin)
    print "Case #%d: %s" % (case_index, r)
  fin.close()
