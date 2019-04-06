import sys

def solve(path):
    new_path = ""
    for step in path:
        if step == "E":
            new_path += "S"
        else:
            new_path += "E"
    return new_path

data = sys.stdin.read().split()
for i in range(int(data.pop(0))):
    n = int(data.pop(0))
    path = data.pop(0)
    path = solve(path)
    print("Case #%d: %s" % (i+1, path))
