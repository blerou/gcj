import sys
import re

NORTH = (-1, 0)
WEST = (0, -1)
EAST = (0, 1)
SOUTH = (1, 0)

def fgets(f):
  return f.readline().rstrip("\n")

def print_map(dmap, H, W):
  """
  elnevezesi terkep kiiratasa
  """
  m = []
  for i in range(H):
    m.append(" ".join([v for k, v in dmap[i].iteritems()]))
  
  return "\n".join(m)

def lowest_neighbor(emap, pos):
  """
  eredeti terkep alapja (emap) meghatarozza, hova folyik innen a viz (pos)
  return a cel regio vagy None sink eseten
  """
  order = [NORTH, WEST, EAST, SOUTH]
  lpos = None
  alt = emap[pos[0]][pos[1]]
  for o in order:
    p = (o[0]+pos[0], o[1]+pos[1])
    if p[0] in emap.keys() and p[1] in emap[p[0]].keys() and emap[p[0]][p[1]] < alt:
      alt = emap[p[0]][p[1]]
      lpos = p
  return lpos

def flow_from(tmap, dmap, pos, H, W):
  """
  folyasirany terkep (tmap) alapjan
  azon helyek meghatarozasa (ret)
  ahonnan ide (pos) folyik a viz
  
  csak akkor kell felvenni, ha meg nincs fent
  az elnevezesi terkepen (dmap)
  """
  ret = []
  for i in range(H):
    for j in range(W):
      if tmap[i][j] == pos:
        if j not in dmap[i].keys():
          ret.append((i, j))
  return ret

def solve_case(emap, H, W):
  """
  sinkek es folyasiranyok (tmap) meghatarozasa
  """
  sinks = []
  tmap = {}
  for i in range(H):
    tmap[i] = {}
    for j in range(W):
      tmap[i][j] = lowest_neighbor(emap, (i, j))
      if tmap[i][j] == None:
        sinks.append((i, j))
  
  """
  sinkekbol kiindulva 
  elnevezesi terkep (dmap) meghatarozasa 
  folyasiranyok (tmap) alapjan
  """
  dmap = [{} for i in range(H)]
  spool = [chr(i+97) for i in range(26)]
  for sink in sinks:
    q = [sink]
    sid = spool.pop(0)
    dmap[sink[0]][sink[1]] = sid
    while len(q):
      pos = q.pop(0)
      for f in flow_from(tmap, dmap, pos, H, W):
        dmap[f[0]][f[1]] = sid
        q.append(f)
  
  return print_map(dmap, H, W)

if __name__ == '__main__':
  fin = open(sys.argv[1], 'r')
  fout = open(sys.argv[1]+'.out', 'w')
  
  for case_index in range(int(fgets(fin))):
    H, W = map(int, re.findall('\d+', fgets(fin)))
    emap = []
    for i in range(H):
      tmp = []
      m = map(int, re.findall('\d+', fgets(fin)))
      for j in range(W):
        tmp.append((j, m[j]))
      emap.append((i, dict(tmp)))
    
    dmap = solve_case(dict(emap), H, W)
    r = "Case #%d:\n%s" % (case_index + 1, dmap)
    print r
    #fout.write(r + "\n")
    
  fin.close()
  fout.close()
