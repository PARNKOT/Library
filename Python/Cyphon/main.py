import functools
import timeit

import helloworld as hw


def test(x):
    y = 1
    for i in range(x):
        y *= i
    return y


def test1(x):
    if x > 1:
        return functools.reduce(lambda a, b: a*b, range(1, x+1))
    return 1

#print(hw.test(4))

#print(test1(4))

#t1 = timeit.timeit("[test(x) for x in range(10)]", setup="from __main__ import test")
#t2 = timeit.timeit("[test(x) for x in range(10)]", setup="from helloworld import test")
#t3 = timeit.timeit("[test1(x) for x in range(10)]", setup="import functools; from __main__ import test1")
#print(t1)
#print(t2)
#print(t3)