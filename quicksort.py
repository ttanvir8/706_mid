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


def quicksort(arr):
    print('############## quicksort start')
    count = 1
    print(f"this is = {count}")
    print(arr)
    if len(arr) <= 1:
        print(f"nothing and length={len(arr)}, {arr}")
        return arr

    left, pivot_list, right = partition(arr)
    left_sorted = quicksort(left)
    right_sorted = quicksort(right)
    count = count + 1
    print('############## quicksort done')
    return left_sorted + pivot_list + right_sorted


arr = [5, 2, 8, 3, 7, 4]
quicksort(arr)
