#		_________________________
#	       |                         |
#--------------|         Checker         |------------------
#	       |_________________________|
#

class checker:
	check_dict = {'(':')', '{':'}', '[':']'}

	def __init__(self, string = ''):
		self.checking_string = string

	def getString(self, string):
		self.checking_string = string

	def check(self) -> int:
		count = 1
		stack = list()
		for letter in self.checking_string:
			if letter in checker.check_dict:
				stack.append([letter, count])
			elif letter in checker.check_dict.values():
				if not stack:
					return count
				elif letter != checker.check_dict[stack.pop()[0]]:
					return count
			count += 1

		if stack:
			return stack.pop()[1]
		return 0

#		_________________________
#	       |                         |
#--------------|     Filter iterator     |
#	       |_________________________|
#
class filterIterator:
	def __init__(self, filter):
		self.iterList = filter.iterList
		self.iterFunc = filter.iterFunc
		self.judge_func = filter.judge_func
		self.retList = []
		self.i = 0
		self.pos = 0
		self.neg = 0

	def __next__(self):
		while True:
			if self.i < len(self.iterList):	
				self.i += 1
				for func in self.iterFunc:
					if func(self.iterList[self.i-1]):
						self.pos += 1
					else:
						self.neg += 1
				isPassed = self.judge_func(self.pos, self.neg)
				self.pos = 0
				self.neg = 0
				if isPassed:
					return self.iterList[self.i-1]
				#else:
				#	return self.__next__()
			else:
				raise StopIteration
			

class multifilter:
	def judge_half(pos, neg):
		if pos >= neg:
			return True
		return False

	def judge_any(pos, neg):
		if pos >= 1:
			return True
		return False

	def judge_all(pos, neg):
		if neg == 0:
			return True
		return False

	def __init__(self, iterable, *funcs, judge=judge_any):
		self.iterList = iterable
		self.iterFunc = funcs
		self.judge_func = judge

	def __iter__(self):
		return filterIterator(self)


#		_________________________
#	       |                         |
#--------------| simple number generator |
#	       |_________________________|
#

def isSimple(number):
	count = 1
	for i in range(2, number + 1):
		if number % i == 0:
			count += 1
		if count > 2:
			return False
	return True

def primes():
	yield 2
	yield 3
	
	current = 3

	while True:
		current += 2
		if isSimple(current):
			yield current

def primes2():
    i, f = 2, 1  # число и факториал предыдущего числа
    while True:
        if (f + 1) % i == 0:  # проверяем на простоту по теореме Вильсона через факториал
            yield i
        f, i = f * i, i + 1  # сначала пересчитываем факториал для текущего числа, затем увеличиваем число


#		_________________________
#	       |                         |
#--------------|  domain regexp example  |
#	       |_________________________|
#

s = set()
s.update(re.findall(r'<a.*href=[\'\"]([\w.-]+)[\'\"]', text))
s.update(re.findall(r'<a.*href=[\'\"][\w]+:\/\/([\w.-]+)[\b:\/]?.*[\'\"]', text))
domain_list = list(s)
domain_list.sort()
print(*domain_list, sep='\n')


#		_________________________
#	       |                         |
#--------------|   CSV working example   |--------------
#	       |_________________________|
#

import csv
import datetime

crimes = dict()
with open('Crimes.csv','r') as fh:
	reader = csv.reader(fh)
	s = next(reader)
	index_type = s.index('Primary Type')
	index_date = s.index('Date')
	#dt = datetime.datetime.strptime("10/01/2002 12:47:08 PM", "%d/%m/%Y %H:%M:%S %p")	
	#print(dt.year)
	#print(datetime.strptime('10/01/2002 12:47:08'))
	for s in reader:
		if datetime.datetime.strptime(s[index_date], "%m/%d/%Y %H:%M:%S %p").year == 2015:
			if s[index_type] not in crimes:
				crimes[s[index_type]] = 1
			else:
				crimes[s[index_type]] += 1
	
max_crime = ['', 0]
	
for crime in crimes:	
	if crimes[crime] > max_crime[1]:
		max_crime[1] = crimes[crime]
		max_crime[0] = crime

print(max_crime)


#		_________________________
#	       |                         |
#--------------| Parent checking (graph) |--------------
#	       |_________________________|
#

def getTops(dct:'dict') -> dict:
	'''
		Формирует выходной словарь (res), ключ которого (res->key) равен значению первого ключа входного словара (dct[0]),
		а значение (res->value) равно значению второго ключа входного словаря(dct[1]) 
	'''
	res = dict()
	for el in dct:
		res[el] = dct[el]
		for value in dct[el]:
			if value not in res:
				res[value] = []
	return res

def isParent(graph:'dict', parent:'str', child:'str') -> bool:
	'''
		Функция проверяет: является ли 'parent' предком 'child' в графе 'graph'
	'''
	if parent in graph[child]:
		return True
	for top in graph[child]:
		if isParent(graph, parent, top):
			return True
	return False

#print(isParent(data3, 'C', 'F'))

def countParents(graph:'dict', parent) -> int:
	'''
------------------------Function (countParents) doc---------------------------
Function: countParents
Args: 
	1) graph -> dict,
	2) parent -> depends on graph keys and values (str is better choice)
Return: ret -> int

Функция подсчитывает количество наследников элемента 'parent' в графе 'graph' 
------------------------------------------------------------------------------
	'''
	ret = 1
	for top in graph:
		#print(parent, '<-', top, ':', isParent(graph, parent, top))
		if isParent(graph, parent, top):
			ret += 1
	return ret

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Самый первый класс по наследованию. Хранит объект и связь его с вершинами.
# Можно добавить расчет для каждого объекта всех детей (наследников, связанных вершин)
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

#		____________________________
#	       |                            |
#--------------| Stack with Maximum support |--------------
#	       |____________________________|
#


class StackWithMax(list):
    def __init__(self, *lst):
        self.maximum = list()
        self.push(*lst)
        #super().append(lst)

    def push(self, *lst):
        for value in lst:
            if not self:
                self.append(value)
                self.maximum.append(value)
            else:
                if value >= self.maximum[-1]:
                    self.maximum.append(value)
                else:
                    self.maximum.append(self.maximum[-1])
                self.append(value)    

    def pop(self):
        if self:
            super().pop()
            self.maximum.pop()

    def max(self):
        if self:
            return self.maximum[-1]


#		____________________________
#	       |                            |
#--------------| 	  Min Heap 	    |--------------
#	       |____________________________|
#

class Heap(list):
    '''
    Класс, реализующий кучу  в виде бинарного дерева (пока что реализована только минимальная куча).
    Хранится в виде списка.
    '''

    def __init__(self, lst: 'list', isMin = True, max_child = 2):
        self.extend(lst)
        self.max_index = len(lst) - 1
        self.max_child = max_child
        self.isMin = bool(isMin)
        self.make_heap()

    def add(self, *args):
        self.extend(args)
        self.max_index = len(self) - 1
        self.make_heap()

    def make_heap(self:'list'):
        for i in range((self.max_index - 1)//self.max_child, -1, -1):
            self.sift_down(i)

    def sift_down(self, current_index: 'int'):
        while True:
            childs = set()
            for i in range(1, self.max_child + 1):
                ind = self.max_child*current_index + i
                if ind <= self.max_index:
                    childs.add(ind)
                else:
                    break

            tmp = current_index
            for child in childs:
                if self[child]*(-1)**self.isMin > self[tmp]*(-1)**self.isMin:
                    tmp = child

            if tmp != current_index:
                self[current_index], self[tmp] = self[tmp], self[current_index]
            else:
                break

            current_index = tmp

    def sift_up(self, current_index: 'int'):
        while current_index != 0:
            parent_index = (current_index - 1)//self.max_child
            if self[parent_index]*(-1)**self.isMin < self[current_index]*(-1)**self.isMin:
                self[current_index], self[parent_index] = self[parent_index], self[current_index]
            else:
                break

            current_index = parent_index
