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


def select_pivot(arr):
    """Select a random pivot from the array"""
    return random.choice(arr)


def filter_equal(arr, pivot):
    """Find all copies of the pivot"""
    return [x for x in arr if x == pivot]


def parallel_quicksort(arr, result):
    print('############## quicksort start')
    print(arr)
    if len(arr) <= 1:
        print(f"nothing and length={len(arr)}, {arr}")
        result.extend(arr)
        return

    # QUICKSORT algorithm as specified:
    # p <- SELECTPIVOT(S); (Pick a random number 'p')
    p = select_pivot(arr)
    print(f"selected pivot: {p}")

    # e <- FILTER(S, equal to p); (Find all copies of 'p')
    e = filter_equal(arr, p)
    print(f"elements equal to pivot: {e}")

    # Create partitions for smaller and bigger than pivot
    smaller = [x for x in arr if x < p]
    bigger = [x for x in arr if x > p]
    print(f"smaller than pivot: {smaller}")
    print(f"bigger than pivot: {bigger}")

    # l <- QUICKSORT(smaller than p) || r <- QUICKSORT(bigger than p)
    # (Sort the small numbers AND sort the big numbers at the same time!)
    manager = Manager()
    l_result = manager.list()
    r_result = manager.list()

    # Create processes for parallel sorting
    if smaller:
        l_proc = Process(target=parallel_quicksort, args=(smaller, l_result))
        l_proc.start()
    else:
        l_result = []

    if bigger:
        r_proc = Process(target=parallel_quicksort, args=(bigger, r_result))
        r_proc.start()
    else:
        r_result = []

    # Wait for processes to complete
    if smaller:
        l_proc.join()
    if bigger:
        r_proc.join()

    # return FLATTEN(l, e, r) (Stick them together: Left-Middle-Right)
    print('############## quicksort done')
    result.extend(list(l_result) + e + list(r_result))


if __name__ == "__main__":
    arr = [5, 2, 8, 3, 7, 4]
    manager = Manager()
    result = manager.list()
    parallel_quicksort(arr, result)
    print(f"Sorted array: {list(result)}")
