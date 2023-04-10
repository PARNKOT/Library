ticket = input()

def digitSum(str):
  sum = 0
  for i in range(len(str)):
    sum+=int(str[i])
  return sum

if digitSum(ticket[0:3]) == digitSum(ticket[3:]):
  print("Счастливый")
else:
  print("Обычный")

#Version2.0
a, b, c, d, e, f = input()
n= int(a)+int (b)+int(c)
m= int(d)+int (e)+int(f)
if n==m:
    print ('Счастливый')
else:
    print ('Обычный')

#Version3.0
ans = {False: 'Счастливый', True : 'Обычный'}
b,c,d,e,f,g = (int(n) for n in input())
print(ans[bool((b+c+d)-(e+f+g))])