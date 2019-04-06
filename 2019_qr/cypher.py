import sys

pt = sys.argv[1]

print("plaintext:",len(pt),pt)

ps = [9767, 9769, 9781, 9787, 9791, 9803, 9811, 9817, 9829, 9833, 9839, 9851, 9857, 9859, 9871, 9883, 9887, 9901, 9907, 9923, 9929, 9931, 9941, 9949, 9967, 9973]

ptn = []
for c in pt:
    idx = ord(c)-65
    #print(c, idx, ps[idx])
    ptn.append(ps[idx])

print("ptn:",len(ptn),ptn)

ct = []
for i in range(1, len(pt)):
    ct.append(ptn[i-1]*ptn[i])

print("ct:",len(ct))
print(" ".join(map(str, ct)))
