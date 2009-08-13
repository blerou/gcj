import sys
import re
from heapq import heappop
from heapq import heappush

def fgets(f):
  return f.readline().rstrip("\n")


def read_trains(fin, cnt):
  r = []
  for i in range(cnt):
    time = map(int, re.findall('\d+', fgets(fin)))
    r += [(time[0]*60+time[1], time[2]*60+time[3])]
  return r

def SolveCase(case_index, case):
  T, (tripsa, tripsb) = case
  trips = []
  for trip in tripsa:
    trips.append([trip[0], trip[1], 0])
  for trip in tripsb:
    trips.append([trip[0], trip[1], 1])

  trips.sort()

  start = [0, 0]
  trains = [[], []]

  for trip in trips:
    d = trip[2]
    if trains[d] and trains[d][0] <= trip[0]:
      # We're using the earliest train available, and
      # we have to delete it from this station's trains.
      heappop(trains[d])
    else:
      # No train was available for the current trip,
      # so we're adding one.
      start[d] += 1
    # We add an available train in the arriving station at the
    # time of arrival plus the turnaround time.
    heappush(trains[1 - d], trip[1] + T)

  return "Case #%d: %d %d" % (case_index, start[0], start[1])

if __name__ == '__main__':
  fin = open(sys.argv[1], 'r')
  fout = open(sys.argv[2], 'w')
  for c in range(int(fgets(fin))):
    t = int(fgets(fin))
    n = map(int, re.findall('\d+', fgets(fin)))
    case = (t, (read_trains(fin, n[0]), read_trains(fin, n[1])))
    r = SolveCase(c+1, case)
    print r
    fout.write(r + "\n")
  fin.close()
  fout.close()
