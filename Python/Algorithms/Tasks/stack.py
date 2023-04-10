class StackObj:
    def __init__(self, data):
        self.next = None
        self.data = data


class StackIterator:
    def __init__(self, top:StackObj):
        self.current = top

    def __next__(self):
        if self.current == None:
            raise StopIteration
        tmp = self.current
        self.current = self.current.next
        return tmp


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    # Добавляем в конец стэка (next)
    def push_back(self, obj: StackObj):
        if self.top:
            for node in self:
                if not node.next:
                    node.next = obj
        else:
            self.top = obj
        self.count += 1

    # Добавляем в начало стека (top)
    def push_front(self, obj: StackObj):
        if self.top:
            obj.next = self.top
            self.top = obj
        else:
            self.top = obj
        self.count += 1

    def __iter__(self):
        return StackIterator(self.top)

    def __getitem__(self, item):
        if item < 0 or item >= self.count:
            raise IndexError('неверный индекс')
        count = 0
        for obj in self:
            if count == item:
                return obj.data
            count += 1

    def __setitem__(self, key, value):
        if key < 0 or key >= self.count:
            raise IndexError('неверный индекс')
        count = 0
        for obj in self:
            if count == key:
                obj.data = value
                break
            count += 1

    def __len__(self):
        return self.count


if __name__ == "__main__":
    st = Stack()
    st.push_front(StackObj('1'))
    st.push_back(StackObj('2'))
    st.push_back(StackObj('3'))
    st.push_back(StackObj('4'))
    st.push_front(StackObj('5'))
    for obj in st:
        print(obj.data)
    print(st[4])
    print('Length: ', len(st))
