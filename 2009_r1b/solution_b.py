import sys
import re

def solve_case(f):
  num = f.readline().rstrip()
  pos = len(num)-2
  
  while (pos >= 0 and num[pos] >= max(num[pos+1:])):
    pos -= 1
  
  if pos < 0:
    org = num
    num = num.replace('0', '')
    num = re.findall('\d', num)
    num.sort()
    num = ''.join(num)
    while int(num) <= int(org):
      num = num[0:1] + '0' + num[1:]
    num = ''.join(num)
  else:
    cur, cmax = pos+1, 10
    end = num[pos+1:]
    for i in range(len(end)):
      if int(end[i]) > int(num[pos]) and int(end[i]) < cmax:
        cur = i
        cmax = end[i]
    
    tmp = num[pos]
    num = num[:pos] + end[cur]
    end = end[:cur] + tmp + end[cur+1:]
    end = re.findall('\d', end)
    end.sort()
    num = num + ''.join(end)
  return num

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print "Gimme the input file..."
    sys.exit()
  
  fin = open(sys.argv[1], 'r')
  fout = open(sys.argv[1]+'.out', 'w')
  
  for case in range(int(fin.readline())):
    r = solve_case(fin)
    r = "Case #%d: %s" % (case+1, r)
    print r
    fout.write(r+"\n")
  
  fin.close()
  fout.close()

