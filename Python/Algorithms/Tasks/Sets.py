class ParallelSet(dict):
    '''
     Unique id is implemented via minimal element in parallel set
    '''

    def __init__(self):
        pass

    def make_set(self, x):
        self[x] = x

    def find(self, x):
        return self[x]

    def union(self, x, y):
        '''
            Скорость алгоритма: O(n) - алгоритм имеет линейную зависимость от n,
                где n - Общее количество элементов во вех множествах
        :param x:
        :param y:
        :return:
        '''
        idx = self.find(x)
        idy = self.find(y)
        if idx == idy:
            return
        m = min(idx, idy)
        for key, value in self.items():
            if value == idx or value == idy:
                self[key] = m


class ParallelSet_heap(dict):
    def make_set(self, x):
        self[x] = {'id': x, 'rank': 0}  # 0 - rank

    def find(self, x):
        while x != self[x]['id']:
            x = self[x]['id']
        return x

    def union(self, x, y):
        idx = self.find(x)
        idy = self.find(y)
        if idx == idy:
            return
        if self[idx]['rank'] > self[idy]['rank']:
            self[idy]['id'] = idx
        else:
            self[idx]['id'] = idy
            a = self[idx]['rank']
            if self[idx]['rank'] == self[idy]['rank']:
                self[idy]['rank'] += 1


'''
ps = ParallelSet()
ps.make_set(1)
ps.make_set(2)
ps.make_set(3)
ps.make_set(4)
ps.make_set(5)
ps.make_set(6)
ps.make_set(7)
ps.make_set(8)
ps.make_set(9)
print(ps)
ps.union(9,3)
ps.union(9,2)
ps.union(9,4)
ps.union(9,7)
ps.union(6,1)
ps.union(6,8)
print(ps)'''

psh = ParallelSet_heap()
psh.make_set(1)
psh.make_set(2)
psh.make_set(3)
psh.make_set(4)
psh.make_set(5)
psh.make_set(6)
psh.make_set(7)
psh.make_set(8)
psh.make_set(9)
print('psh:', psh)
psh.union(9, 3)
psh.union(9, 2)
psh.union(9, 4)
psh.union(9, 7)
psh.union(6, 1)
psh.union(6, 8)
print(psh.find(2))
print('psh:', psh)
