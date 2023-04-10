n = input()
length = len(n)

if length>=2 and (11<=int(n[length-2:length])<=14): print(n,"программистов")
#if 11<=int(n)<=14: print(n + " программистов")
elif int(n[length-1]) == 1: print(n, "программист")
elif 2<=int(n[length-1])<=4: print(n, "программиста")
elif 5<=int(n[length-1])<=9 or int(n[length-1]) == 0: print(n, "программистов")

#Version 2.0
i=int(input())
d=i%10
h=i%100
if d==1 and h!=11:
    s=""
elif 1<d<5 and not 11<h<15:
    s="а"
else:
    s="ов"
print(i," программист"+s)