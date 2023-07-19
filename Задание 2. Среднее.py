s = ''.join(['1' + str(k + 1) + chr(k + 65) for k in range(26)])
glas = 'AEIOUY'
soglas = 'BCDFGHJKLMNPQRSTVWXZ'
for k in range(26):
  if '1' + str(k + 1) + chr(k + 65) in s and chr(k + 65) in glas:
    s = s.replace('1' + str(k + 1) + chr(k + 65),str(ord(chr(k + 65))),1)
  elif '1' + str(k + 1) + chr(k + 65) in s and chr(k + 65) in soglas:
    s = s.replace('1' + str(k + 1) + chr(k + 65),str(ord(chr(k + 65))),1)
print(sum([int(k) for k in s]))
