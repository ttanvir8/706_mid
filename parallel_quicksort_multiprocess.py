import random
from multiprocessing import Process, Manager


def partition(arr):
    print(f'\n%%%%%%%%%%%%%%%inside partition arr={arr}')
    if len(arr) <= 1:
        print(f"arr is too small to partition, length={len(arr)}, arr={arr}")
        return arr, []
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    print(f"pivot={pivot}, left={left}, right={right}")
    return left, [pivot], right


def parallel_quicksort(arr, result):
    print('############## quicksort start')
    print(arr)
    if len(arr) <= 1:
        print(f"nothing and length={len(arr)}, {arr}")
        result.extend(arr)
        return
    left, pivot_list, right = partition(arr)
    manager = Manager()
    left_result = manager.list()
    right_result = manager.list()
    left_proc = Process(target=parallel_quicksort, args=(left, left_result))
    right_proc = Process(target=parallel_quicksort, args=(right, right_result))
    left_proc.start()
    right_proc.start()
    left_proc.join()
    right_proc.join()
    print('############## quicksort done')
    result.extend(list(left_result) + pivot_list + list(right_result))


if __name__ == "__main__":
    arr = [5, 2, 8, 3, 7, 4]
    manager = Manager()
    result = manager.list()
    parallel_quicksort(arr, result)
    print(f"Sorted array: {list(result)}")
