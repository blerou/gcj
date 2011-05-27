import sys

def fgets(f):
  return f.readline().rstrip("\n")

def _get_match_engine(query, engines):
  for i, e in engines.iteritems():
    if query == e:
      return i

def read_case(f):
  engines = dict([(i, fgets(f)) for i in range(int(fgets(f)))])
  queries = dict([(i, _get_match_engine(fgets(f), engines)) for i in range(int(fgets(f)))])
  return (engines.keys(), queries)

def _has_none_used_engine(engines, queries):
  for e in engines:
    if e not in queries.values():
      return [e]
  return None

def process_case(engines, queries):
  eng = _has_none_used_engine(engines, queries)
  r = []
  while not eng:
    min_eng = dict([(min([p for p, eng in queries.iteritems() if eng == e]), e) for e in engines])
    max_pos = max(min_eng.keys())
    queries = dict([(p, e) for p, e in queries.iteritems() if p >= max_pos])
    r.append(min_eng[max_pos])
    eng = _has_none_used_engine(engines, queries)
  return r + eng

if __name__ == '__main__':
  fin = open(sys.argv[1], 'r')
  fout = open(sys.argv[1]+'.out', 'r')
  for i in range(int(fgets(fin))):
    a = read_case(fin)
    b = process_case(a[0], a[1])
    r = "Case #%s: %d" % (i+1, len(b)-1)
    print r
    fout.write(r+"\n")
  fin.close()
  fout.close()
