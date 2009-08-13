import sys

def fgets(f):
  return f.readline().rstrip("\n")

def main():
  in_name = sys.argv[1]
  fin = open(in_name, 'r')
  for i in range(int(fgets(fin))):
    s = int(fgets(fin))
    for j in range(s):
      fgets(fin)
    cnt = 0
    qs = []
    for q in range(int(fgets(fin))):
      query = fgets(fin)
      if query not in qs:
        if len(qs) == s-1:
          cnt += 1
          qs = []
        qs.append(query)
    print "Case #%d: %d" % (i+1, cnt)
  fin.close()

if __name__ == '__main__':
  main()