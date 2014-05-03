import sys


def read_input():
    s = sys.stdin.read()
    data = filter(len, s.replace("\n", " ").split(" "))
    T = int(data.pop(0))
    for _ in range(T):
        [N, L], data = map(int, data[0:2]), data[2:]
        outlets, data = data[0:N], data[N:]
        devices, data = data[0:N], data[N:]
        yield L, outlets, devices

def switches(L):
    for l in range(0, L+1):
        for i in range(0, L-l):
            

def solve(c):
    L, outlets, devices = c
    
    return "NOT POSSIBLE"

if __name__ == "__main__":
    idx = 1
    for c in read_input():
        print "Case #%d: %s" % (idx, solve(c))
        idx += 1
