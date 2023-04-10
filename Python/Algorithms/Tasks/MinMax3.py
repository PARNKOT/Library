a,b,c = int(input()), int(input()), int(input())

Nmin = min(a,b,c)
Nmax = max(a,b,c)
'''
if a == Nmax:
  print(a)
  if b == Nmin: print(b,c,sep='\n')
  else:         print(c,b,sep='\n')
elif b == Nmax:
  print(b)
  if a == Nmin: print(a,c,sep='\n')
  else:         print(c,a,sep='\n')
elif c == Nmax:
  print(c)
  if a == Nmin: print(a,b,sep='\n')
  else:         print(b,a,sep='\n')
'''

print(Nmax, Nmin, a+b+c-Nmin-Nmax, sep='\n')