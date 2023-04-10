'''
class ExtendedStack(list):
    def sum(self):
        # операция сложения
        self.append(self.pop() + self.pop())

    def sub(self):
        # операция вычитания
        self.append(self.pop() - self.pop())
    
    def mul(self):
        # операция умножения
        self.append(self.pop() * self.pop())

    def div(self):
        # операция целочисленного деления
        self.append(self.pop() // self.pop())

es = ExtendedStack()
for i in range(5):
    es.append(i+1)
print(es)

es.sum()
print(es)
es.sub()
print(es)
es.mul()
print(es)
es.div()
print(es)
'''
#              _________
#             |         |
#-------------| Task #3 |-------------
#             |_________|
'''
import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, x):
        # 1) super(Loggablelist,self).append(x)
        # 2) super(Loggablelist).append(self,x)
        super(Loggablelist,self).append(x)
        self.log(x)
'''
#class Loggablelist(list, Loggable):
#    def append(self, x):
#        # 1) super(Loggablelist,self).append(x)
#        # 2) super(Loggablelist).append(self,x)
#        super().append(x)
#        self.log(x)
'''
ll = Loggablelist()
ll.append('Egor')
ll.append('Sonya')
print(ll)
'''

'''
def foo():
    raise ZeroDivisionError

try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")
'''
'''
class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError()

ps = PositiveList()
try:
    ps.append(1)
    ps.append(2)
    ps.append(3)
    ps.append(0)

except NonPositiveError:
    print(ps)
'''

import socket
try:
    print(socket.if_nameindex())
except socket.OSError:
    print('Oops!')

