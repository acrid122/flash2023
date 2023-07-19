s = ''
for k in range(60):
  s += '2002' if k % 2 == 0 else '3003'
while '2002' in s or '3003' in s:
  if '2002' in s:
    s = s.replace('2002', '23', 1)
  elif '3003' in s:
    s = s.replace('3003', '00', 1)
print(s.count('3002'))
