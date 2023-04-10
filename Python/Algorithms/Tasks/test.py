import time

'''
classes = dict()

#Заполняем дерево наследований
for _ in range(int(input())):
	child, parent = input().strip().split(':')
	if parent not in classes:
		classes[parent] = {'children':set()}
	classes[parent]['children'].add(child) 
	print(classes)

#Поиск по дереву
for _ in range(int(input())):
'''

#----------- V2.0 --------------

'''
class Link:
	def __init__(self, name):
		self.binded_list = set()
		self.name = name

	def bind(self, link):
		for el in link.binded_list:
			self.binded_list.add(el)
		for el in self.binded_list:
			self.binded_list.add(el)
		
		self.binded_list.add(link.name)
		link.binded_list.add(self.name)

A = Link('A')
B = Link('B')
C = Link('C')
A.bind(B)
C.bind(B)
print(A.binded_list)
print(B.binded_list)
print(C.binded_list)
'''

#----------- V3.0 --------------
classes = set()

class Link:
	def __init__(self, name):
		self.parents = set()
		self.name = name

	def derive(self, parent):
		self.parents.add(parent.name)
		for el in parent.parents:
			self.parents.add(el)

for _ in range(int(input())):
	inp = input().split()
	#inp = inp.split(':')

	for i in range(len(inp)):
		inp[i] = inp[i].strip()
	
	child = inp[0]
	parent = inp[1:]	
	#child, parent = inp.split(':')
	
	lkChild = Link(child)
	for par in parent:
		if classes:
			for el in classes:
				if el.name == par:
					lkParent = el
					#print(el.name)
		else:
			lkParent = Link(par)

		#print('Parent:', lkParent.name)
		lkChild.derive(lkParent)

		if lkParent not in classes:
			classes.add(lkParent)
		classes.add(lkChild)
		print(lkParent.parents)
		print(lkChild.parents)

for _ in range(int(input())):
	parent, child = input().split()
	for el in classes:
		if el.name == child:
			if parent in el.parents:
				print('Yes')
			else:
				print('No')
			break

'''
A = Link('A')
B = Link('B')
C = Link('C')

B.derive(A)
C.derive(B)
print(A.parents)
print(B.parents)
print(C.parents)
'''

'''
	#-------DEBUG-------
	if inp == 'debug':
		print("Debug mode is ON!")
		while True:	
			command = input().split()
			if command[0] == 'show':
				for el in classes:
					if el.name == command[1]:
						print(el.parents)
						break
			elif command[0] == 'exit':
				print("Debug mode is OFF")
				inp = input()
				break
	#-------DEBUG-------
'''