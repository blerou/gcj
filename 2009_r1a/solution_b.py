import sys
import re

BLOCK = 2
CROSS = 1

def fgets(f):
  return f.readline().rstrip("\n")

def prepare(f):
  N, M = map(int, re.findall('\d', fgets(f)))
  ls = []
  for n in range(N):
    ls.append(map(int, re.findall('\d', fgets(f))))
  lights = []
  for light in ls:
    l = []
    for m in range(M):
      l.append(light[m*3:(m+1)*3])
    lights.append(l)
  return (N, M, lights)

def solve_case(f):
  N, M, lights = prepare(f)
  #print lights
  for n in range(N-1, -1, -1):
    if n == N-1:
      ss = [[] for _ in range(M*2)]
      ss[0] = [0]
    else:
      ss = [[i+BLOCK] for i in ns]
    # deli oldal 1
    for m in range(1, M*2):
      t = min(ss[m-1])
      min_ct = lights[n][m/2][2] + lights[n][m/2][0]
      sum_ct = sum(lights[n][m/2][1:3])
      good_ct = lights[n][m/2][1]
      dly_ct = lights[n][m/2][0]
      if t < min_ct:
        t = min_ct
      elif (t - min_ct) % sum_ct < good_ct:
        t += dly_ct
      ss[m].append(t+CROSS)
    # eszaki oldal
    ns = [[sys.maxint] for _ in range(M*2)]
    # delrol 1
    for m in range(M*2-1):
      t = min(ss[m])
      min_ct = lights[n][m/2][2]
      sum_ct = sum(lights[n][m/2][1:3])
      good_ct = lights[n][m/2][0]
      dly_ct = lights[n][m/2][1]
      if t < min_ct:
        t = min_ct
      elif (t - min_ct) % sum_ct > good_ct:
        t += dly_ct
      ns[m+1].append(t+CROSS)
    # sorban 0
    for m in range(1, M*2):
      t = min(ns[m-1])
      min_ct = lights[n][m/2][2] + lights[n][m/2][0]
      sum_ct = sum(lights[n][m/2][1:3])
      good_ct = lights[n][m/2][1]
      dly_ct = lights[n][m/2][0]
      if t < min_ct:
        t = min_ct
      elif (t - min_ct) % sum_ct > good_ct:
        t += dly_ct
      ns[m].append(t+CROSS)
    print ns
  return min(ns[M*2-1])

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print "Gimme the input file..."
    sys.exit()
  
  fin = open(sys.argv[1], 'r')
  fout = open(sys.argv[1]+'.out', 'w')
  
  for case_index in range(int(fgets(fin))):
    r = solve_case(fin)
    r = "Case #%d: %s" % (case_index+1, r)
    print r
    fout.write("%s\n" % (r,))
  
  fin.close()
  fout.close()

