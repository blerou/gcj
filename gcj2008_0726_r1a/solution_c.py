import sys
import math

def fgets(f):
  return f.readline().rstrip("\n")

def get_binomials(n):
  o = { 0: 1 }
  r = []
  for row in range(0, n):
    r = dict([(i, o[i - 1] + o[i]) for i in range(1, len(o))])
    r[0], r[len(o)] = 1, 1
    o = r
  return o

def factorial(n):
  f = 1
  while (n > 0):
    f = f * n
    n = n - 1
  return f

def pow(x, n):
  if n == 0:
    return 1
  a = x
  for i in xrange(1, n):
    a *= x
    a = a % 1000
  return a

def solve_case(n):
  r = 0
  for i, m in get_binomials(n).iteritems():
    t = m * pow(3, n - i) * pow(5, i / 2) * pow(math.sqrt(5), i % 2)
    r += t
    r = r % 1000
  return int(r)



def get_max_coef(n):
  i = int(math.sqrt(n))
  while i > 1:
    if n % i == 0:
      return i
    i = i - 1
  return n

def solve_case2(n):
  """
  x^n = x^(i*k + j)     where i = int(sqrt(n)), k = n / i, j = n % i
      = (x^i)^k * x^j   so primes will be ignored :)
  """
  x = 3 + math.sqrt(5)
  i = int(math.sqrt(n))
  k, j = n, 0
  if i > 4:
    k = n / i
    j = n % i
    x = pow(x, i)
  r = pow(x, k) * pow(x, j)
  return r % 1000
  
if __name__ == "__main__":
  fin = open(sys.argv[1], 'r')
  for case_index in range(1, int(fgets(fin)) + 1):
    r = solve_case2(int(fgets(fin)))
    print 'Case #%d: %03d' % (case_index, r)
