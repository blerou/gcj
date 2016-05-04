import sys
import math

DEBUG=False

def read_input():
    data = sys.stdin.read().split()
    for _ in xrange(int(data.pop(0))):
        n = int(data.pop(0))
        j = int(data.pop(0))
        yield n, j

primes = [2]

def divisor(i):
    t = math.sqrt(i)
    for p in primes:
        if p > t: break
        if i % p == 0:
            return p
    return None

def gen_primes(n):
    global primes
    for i in xrange(3,n+1,2):
        if not divisor(i):
            primes.append(i)

def gen_strings(n):
    for i in xrange(2**(n-1)+1, 2**n, 2):
        yield bin(i)[2:]

def divisors(s):
    ds = []
    for b in xrange(2,11):
        n = int(s, b)
        d = divisor(n)
        if not d: break
        ds.append(d)
    if len(ds) < 9:
        return None
    else:
        return ds
        
def solve(data):
    n, j = data
    if DEBUG: print "start", n, j
    result = []
    for s in gen_strings(n):
        if len(result) == j: break
        ds = divisors(s)
        if ds:
            result.append((s, ds))
    return "\n".join(["%s %s" % (s, " ".join(map(str, ds))) for s, ds in result])

if __name__ == "__main__":
    gen_primes(100000)
    i = 1
    for c in read_input():
        print "Case #%d:\n%s" % (i, solve(c))
        i += 1

2,1

   12
GG GG
GL GL
LG LG
LL LL

2,2
    2
GG GGGG
GL GGGL
LG LGGG
LL LLLL

2,3
    2
GG GGGGGGGG
GL GGGGGGGL
LG LGGGGGGG
LL LLLLLLLL

3,2
     2   6
GGG GGGGGGGGG
GGL GGGGGGGGL
GLG GGGGLGGGG
GLL GGGGLLGLL
LGG LGGGGGGGG
LGL LGLGGGLGL
LLG LLGLLGGGG
LLL LLLLLLLLL

3,3
         6
GGG GGGGGGGGGGGGGGGGGGGGGGGGGGG
GGL GGGGGGGGGGGGGGGGGGGGGGGGGGL
GLG GGGGGGGGGGGGGLGGGGGGGGGGGGG
GLL GGGGGGGGGGGGGLLGLLGGGGLLGLL
LGG LGGGGGGGGGGGGGGGGGGGGGGGGGG
LGL LGLGGGLGLGGGGGGGGGLGLGGGLGL
LLG LLGLLGGGGLLGLLGGGGGGGGGGGGG
LLL LLLLLLLLLLLLLLLLLLLLLLLLLLL

4,2
      .         .     2,12
GGGG GGGGGGGGGGGGGGGG
GGGL GGGGGGGGGGGGGGGL
GGLG GGGGGGGGGGLGGGGG
GGLL GGGGGGGGGGLLGGLL
GLGG GGGGGLGGGGGGGGGG
GLGL GGGGGLGLGGGGGLGL
GLLG GGGGGLLGGLLGGGGG
GLLL GGGGGLLLGLLLGLLL
LGGG LGGGGGGGGGGGGGGG
LGGL LGGLGGGGGGGGLGGL
LGLG LGLGGGGGLGLGGGGG
LGLL LGLLGGGGLGLLLGLL
LLGG LLGGLLGGGGGGGGGG
LLGL LLGLLLGLGGGGLLGL
LLLG LLLGLLLGLLLGLLLG
LLLL LLLLLLLLLLLLLLLL


(when k <= c -> one position @ 2*k ???)


