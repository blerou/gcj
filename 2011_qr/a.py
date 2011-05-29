#!/usr/bin/python

import sys
import re

def fgets(f):
    return f.readline().rstrip("\n")

def parse_pair(x):
   x = re.split(' ', x)
   return (x[0], int(x[1]))

def parse(input):
    input = re.split(' (?=[OB])', input)
    input = map(parse_pair, input) 
    result = []
    positions = {'B': 1, 'O': 1}
    for (robot, button_pos) in input:
        result.append((robot, abs(positions[robot] - button_pos) + 1))
        positions[robot] = button_pos
    return result

def solve(input):
    curr_robot = 'B'
    curr_time = 0
    sum = 0
    for (r, t) in input:
        if r == curr_robot:
            curr_time += t
        else:
            sum += curr_time
            curr_robot = r
            if t <= curr_time:
                curr_time = 1
            else:
                curr_time = t - curr_time
    return sum + curr_time

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[1]+'.out', 'w')

    cases = int(fgets(fin))
    for case in range(cases):
        input = fgets(fin)
        input = re.sub('^\d+ ', '', input)
        res = "Case #%d: %d\n" % (case+1, solve(parse(input)))
        fout.write(res)
        print res
        
    fin.close()
    fout.close()
