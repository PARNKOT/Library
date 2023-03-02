import random
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Queue
from MergeSort import merge_sort, merge_sorted_arrays


def mul(numbers):
    return numbers[0] * numbers[1]


def merge_sort_multiprocess(arr_sort):
    merge_sort(arr_sort)
    return arr_sort


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f"{func} time: {time.time() - start}")

    return wrapper


def split_arr(arr, parts=2):
    length = len(arr)
    step = length//parts
    out = [arr[step*i:step*(i+1)] for i in range(parts)]
    for i in range(step*parts-length, 0):
        out[-1].append(arr[i])
    return out


def sort_multiprocess(arr, max_workers=2):
    executor = ProcessPoolExecutor(max_workers=max_workers)
    arr_splited = split_arr(arr, parts=2)#[arr[:n // 2], arr[n // 2:]]
    # arr_l = arr[:n//2]
    # arr_r = arr[n//2:]
    for index, some in enumerate(executor.map(merge_sort_multiprocess, arr_splited)):
        arr_splited[index] = some

    merge_sorted_arrays(*arr_splited, arr)
    #print(arr)


@timed
def sort_one_thread(arr):
    merge_sort(arr)
    #print(arr)


if __name__ == "__main__":
    n = 10000
    #executor = ThreadPoolExecutor(max_workers=2)
    #executor = ProcessPoolExecutor(max_workers=2)
    arr = [random.randint(1, n) for _ in range(n)]
    #sort_one_thread(arr.copy())

    #start = time.time()
    #arr_l = arr[:n//2]
    #arr_r = arr[n//2:]
    #sort_multiprocess(arr_l)
    #sort_multiprocess(arr_r)
    #merge_sorted_arrays(arr_l, arr_r, arr)
    #sort_multiprocess(arr, max_workers=2)
    #print(f"time: {time.time() - start}")

    start = time.time()
    arr.copy().sort()
    print(f"time: {time.time() - start}")
    

    #for some in executor.map(mul, [(2, 3), (4, 10)]):
    #    print(some)

