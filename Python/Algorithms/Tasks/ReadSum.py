list1 = [] 
list2 = []

while sum(list1) != 0 or not list1:
  s = int(input())
  list1.append(s)
  list2.append(s**2)

print(sum(list2))

#Version2.0
s=[int(input())]
while sum(s)!=0: s.append(int(input()))
print(sum([i**2 for i in s]))