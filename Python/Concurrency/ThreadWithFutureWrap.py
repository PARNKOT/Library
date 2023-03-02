import threading
from concurrent.futures import ThreadPoolExecutor
import time


def test(a, b, delay=0):
    time.sleep(delay)
    print(f"{threading.current_thread().name}: {a+b}")
    return a + b


if __name__ == "__main__":
    executor = ThreadPoolExecutor(max_workers=3)
    executor.submit(test, 2, 3, 3).add_done_callback(lambda x: print(x.result()))
    executor.submit(test, 6, 10, 2).add_done_callback(lambda x: print(x.result()))
    executor.submit(test, 6, 4, 1).add_done_callback(lambda x: print(x.result()))
    #target.add_done_callback(lambda x: print(x.result()))
    #t = threading.Thread(target=target)
    #t.start()
    #t.join()
