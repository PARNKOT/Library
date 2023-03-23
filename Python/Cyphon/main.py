import timeit

import helloworld as hw


def test(x):
    y = 1
    for i in range(x):
        y *= i
    return y


#print(hw.test(4))

t1 = timeit.timeit("[test(x) for x in range(10)]", setup="from __main__ import test")
t2 = timeit.timeit("[test(x) for x in range(10)]", setup="from helloworld import test")
print(t1)
print(t2)