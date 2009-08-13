import sys
import re

def fgets(f):
  return f.readline().rstrip("\n")

def read_trains(fin, cnt, t):
  d, a = [], []
  for i in range(cnt):
    dh, dm, ah, am = map(int, re.findall('\d+', fgets(fin)))
    dt = (dh * 60 + dm) % (24 * 60)
    at = (ah * 60 + am + t) % (24 * 60)

    dt = dh * 60 + dm
    at = ah * 60 + am + t
    
    d.extend([(dt, 0)])
    a.extend([(at, 1)])
  return (d, a)

def cmp_train(a, b):
  r = cmp(a[0], b[0])
  if r == 0:
    r = cmp(b[1], a[1])
  return r

def sum_trains(trains):
  n, c = 0, 0
  trains.sort(cmp_train)
  for t in trains:
    if t[1]:
      c += 1
    elif c:
      c -= 1
    else:
      n += 1
  return n

if __name__ == '__main__':
  fin = open(sys.argv[1], 'r')
  fout = open(sys.argv[1]+'.out', 'w')
  for case in range(1, int(fgets(fin)) + 1):
    t = int(fgets(fin))
    na, nb = map(int, re.findall('\d+', fgets(fin)))
    a, b = [], []
    a_add, b_add = read_trains(fin, na, t)
    a.extend(a_add)
    b.extend(b_add)
    b_add, a_add = read_trains(fin, nb, t)
    a.extend(a_add)
    b.extend(b_add)
    r = "Case #%d: %d %d" % (case, sum_trains(a), sum_trains(b))
    print r
    fout.write(r + "\n")
  fin.close()
  fout.close()
