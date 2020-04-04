import sys

def solve(tt):
    fp = set(["C", "J"])
    duty = {}
    try:
        r = ["" for _ in range(len(tt))]
        for t in sorted(tt):
            ptime, ptype, pidx = t
            if ptype == "start":
                duty[pidx] = fp.pop()
                r[pidx] = duty[pidx]
            elif ptype == "end":
                fp.add(duty[pidx])
                del duty[pidx]
        return "".join(r)
    except KeyError:
        return "IMPOSSIBLE"

t = int(sys.stdin.readline())
for i in range(1, t+1):
    n = int(sys.stdin.readline())
    tt = []
    for j in range(n):
        s, e = sys.stdin.readline().split(" ")
        tt.append((int(s), "start", j))
        tt.append((int(e), "end", j))
    print("Case #%d: %s" % (i, solve(tt)))
