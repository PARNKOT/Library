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
            self.maximum.pop()
            return super().pop()

    def max(self):
        if self:
            return self.maximum[-1]

stack1, stack2 = StackWithMax(), StackWithMax()
n = int(input())
inp = [int(i) for i in input().split()]
m = int(input())
maxres = list()

for value in inp:
    stack1.push(value)
    if stack2:
        maxres.append(max(stack1.max(), stack2.max()))
        stack2.pop()
    else:
        if len(stack1) == m:
            for i in range(m):
                stack2.push(stack1.pop())
            maxres.append(stack2.max())
            stack2.pop()

print(*maxres)
