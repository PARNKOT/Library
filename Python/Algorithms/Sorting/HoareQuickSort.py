import random


def quick_sort_hoare(arr):
    if len(arr) > 1:
        base = random.choice(arr)
        low = [el for el in arr if el < base]
        eq = [el for el in arr if el == base]
        high = [el for el in arr if el > base]

        arr = quick_sort_hoare(low) + eq + quick_sort_hoare(high)

    return arr


if __name__ == "__main__":
    arr = [random.randint(-10, 10) for _ in range(30)]
    print(arr)
    print(quick_sort_hoare(arr))
