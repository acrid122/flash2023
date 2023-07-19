s = ''
for k in range(1, 100, 2):
  s += str(k) + '>' + str(k+1)
while '5>' in s or '3>' in s:
  s = s.replace('5>', '>6', 1)
  s = s.replace('4>', '>5', 1)
  s = s.replace('3>', '>4', 1)
  s = s.replace('2>', '>3', 1)
  s = s.replace('1>', '>2', 1)
k = s.split('>')
count = 0
for i in range(len(k) - 1):
  if k[i] > k[i + 1]:
    count+=1
print(count)
