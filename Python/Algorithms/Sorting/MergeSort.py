# Recursive MergeSort


def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr)//2

        left_arr = arr[:middle]
        right_arr = arr[middle:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        left_index = right_index = current_index = 0

        while left_index < len(left_arr) and right_index < len(right_arr):
            if left_arr[left_index] < right_arr[right_index]:
                arr[current_index] = left_arr[left_index]
                left_index += 1
            else:
                arr[current_index] = right_arr[right_index]
                right_index +=1

            current_index +=1

        while left_index < len(left_arr):
            arr[current_index] = left_arr[left_index]
            left_index += 1
            current_index += 1

        while right_index < len(right_arr):
            arr[current_index] = right_arr[right_index]
            right_index += 1
            current_index += 1


def merge_sorted_arrays(arr_left, arr_right, arr_out):
    left_index = right_index = current_index = 0

    while left_index < len(arr_left) and right_index < len(arr_right):
        if arr_left[left_index] < arr_right[right_index]:
            arr_out[current_index] = arr_left[left_index]
            left_index += 1
        else:
            arr_out[current_index] = arr_right[right_index]
            right_index += 1

        current_index += 1

    while left_index < len(arr_left):
        arr_out[current_index] = arr_left[left_index]
        left_index += 1
        current_index += 1

    while right_index < len(arr_right):
        arr_out[current_index] = arr_right[right_index]
        right_index += 1
        current_index += 1


if __name__ == "__main__":
    sort_list = [7, 6, 4, 5, 2, 3, 1]
    print(sort_list)
    merge_sort(sort_list)
    print(sort_list)
