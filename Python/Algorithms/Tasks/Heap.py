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

    def rank(self):
        count = 1
        i = 0
        length = self.max_index + 1
        if length == 1:
            return 1
        else:
            while True:
                i += 1
                add = self.max_child**i
                count += add
                if count >= length:
                    return i + 1

    def print_tree(self):
        rank = self.rank()
        for i in range(rank-1):
            print('\t'*(rank - i), end='')
            index = self.max_child**i
            print('\t'.join([str(num) for num in self[index-1:2*index-1]]))
        index = self.max_child**(self.rank() - 1)
        print('\t'.join([str(num) for num in self[index-1:]]))

        
#l = [7, 6, 5, 4, 3, 2]
#l.extend((10,11,12))
l = list()
N = 21
for i in range(N):
    l.append(N-1 - i + 1)

#ls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
h1 = Heap(l, max_child=2)
#print(l)
print(h1)
print('Max index:', h1.max_index)
print('Heap rank =', h1.rank())
h1.print_tree()
