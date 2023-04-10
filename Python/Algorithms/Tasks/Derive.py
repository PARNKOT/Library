import sys
sys.stdin = open("result.txt", "r")
lst_mro = [  # список введённых строк
    'G : F',  # сначала отнаследуем от F, потом его объявим, корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
    'A',
    'B : A',
    'C : A',
    'D : B C',
    'E : D',
    'F : D',
    # а теперь другая ветка наследования
    'X',
    'Y : X A',  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
    'Z : X',
    'V : Z Y',
    'W : V',
]

lst_q = [  # список введённых запросов
    'A G',      # Yes   # A предок G через B/C, D, F
    'A Z',      # No    # Y потомок A, но не Y
    'A W',      # Yes   # A предок W через Y, V
    'X W',      # Yes   # X предок W через Y, V
    'X QWE',    # No    # нет такого класса QWE
    'A X',      # No    # классы есть, но они нет родства :)
    'X X',      # Yes   # родитель он же потомок
    '1 1',      # No    # несуществующий класс
]


classes = set()


class Link:
    def __init__(self, name):
        self.bind_list = set()
        self.name = name

    def bind(self, *parent):
        for par in parent:
            self.bind_list.add(par)
        # par.bind_list.add(self)

    def isParent(self, parent):
        if self == parent:
            return True
        if parent in self.bind_list:
            return True
        else:
            for link in self.bind_list:
                if link.isParent(parent):
                    return True
            return False


#___________________Наследуем___________________
#for inp in lst_mro:
for _ in range(int(input())):
	inp = input()
	inp = inp.split(':')
	if len(inp) == 1:
		isFound = False
		for el in classes:
			if el.name == inp[0]:
				isFound = True
				break
		if not isFound:
			classes.add(Link(inp[0]))
	else:
		#inp = inp.split(':')
		for i in range(len(inp)):
			inp[i] = inp[i].strip()
			#print(word)

		tmpPar = set()

		isFound = False
		for el in classes:
			if el.name == inp[0]:
				lkChild = el
				isFound = True
		if not isFound:
			lkChild = Link(inp[0])
			classes.add(lkChild)

		for par in inp[1].split():
			isFound = False
			for el in classes:
				if el.name == par:
					tmpPar.add(el)
					isFound = True
					break
			if not isFound:
				lkParent = Link(par)
				classes.add(lkParent)
				tmpPar.add(lkParent)

		lkChild.bind(*tmpPar)


#___________________Проверяем___________________
for _ in range(int(input())):
#for inp in lst_q:
	parent, child = input().split()
	parent = parent.strip()
	child = child.strip()

	for el in classes:
		if el.name == parent:
			lkParent = el
		if el.name == child:
			lkChild = el
	if Link.isParent(lkChild, lkParent):
		print(lkParent.name,',',lkChild.name,':','Yes')
	else:
		print(lkParent.name,',',lkChild.name,':','No')






'''
A = Link('A')
B = Link('B')
C = Link('C')
Y = Link('Y')
Z = Link('Z')
D = Link('D')
E = Link('E')
F = Link('F')
G = Link('G')
V = Link('V')
W = Link('W')
X = Link('X')

B.bind(A)
C.bind(A)
# D.bind(B)
D.bind(C, B)
E.bind(D)
F.bind(D)
G.bind(F)
Y.bind(X)
Z.bind(X)
# V.bind(Y)
V.bind(Y, Z)
W.bind(V)
Y.bind(A)

print('A G', G.isParent(A))
print('A Z', Z.isParent(A))
print('A W', W.isParent(A))
print('X W', W.isParent(X))
# print('X QWE', QWE.isParent(A))
print('A X', X.isParent(A))
print('X X', X.isParent(X))
print('D A', D.isParent(A))
# print('1 1', G.isParent(A))
'''