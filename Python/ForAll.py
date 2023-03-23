import math
import time
import helloworld
import numpy as np


N = 100


def test(n):
    for i in range(n):
        print(f"tan({i}) : {math.tan(i)}")


def main(func):
    start = time.time()
    func(N)
    print(time.time() - start)


if __name__ == "__main__":
    #main(test)
    #main(helloworld.test)
    print(helloworld.test(10))

