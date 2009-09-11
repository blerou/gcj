import sys
import re

def fgets(f):
  return f.readline().rstrip("\n")

def build_pairs(f, M):
  pairs = []
  for _ in range(M):
    cnt = map(int, re.findall('\d+', fgets(f)))
    p, cnt = cnt[1:], cnt[0]
    pairs.append([(p[i*2], p[i*2+1]) for i in range(cnt)]) 
  return pairs

def build_mix(N, M, pairs):
  base_mix = [dict([(n+1, None) for n in range(N)])]
  for customer in pairs:
    for flav, malt in customer:
      new_mix = []
      for m in base_mix:
        if m[flav] == malt:
          new_mix.append(m)
        if m[flav] == None:
          m[flav] = malt
          new_mix.append(m)
      print base_mix
      print new_mix
      base_mix = new_mix
  
  print base_mix
  return
  
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

def solve_case(fin):
  N, M = int(fgets(fin)), int(fgets(fin))
  
  pairs = build_pairs(fin, M)
  
  mix = build_mix(N, M, pairs)
  
if __name__ == '__main__':
  fin = open(sys.argv[1], 'r')
  for case_index in range(1, int(fgets(fin)) + 1):
    r = solve_case(fin)
    print "Case #%d: %s" % (case_index, r)
  fin.close()
