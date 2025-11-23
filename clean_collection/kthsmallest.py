import random


def selectPivot(A, depth=0):
    """Select a pivot element from array A"""
    indent = "  " * depth

    if len(A) == 0:
        return None
    elif len(A) == 1:
        pivot = A[0]
        return pivot
    else:
        # For better performance, randomly select from a sample
        # For simplicity, we'll use the first element or random if array is large
        if len(A) > 10:
            # Random selection from a sample for better pivot choice
            sample_size = min(5, len(A))
            sample = random.sample(A, sample_size)
            pivot = random.choice(sample)
        else:
            # For small arrays, use first element
            pivot = A[0]

        return pivot


def kthSmallest(A, k, f, I, depth=0):
    
    """Find the k-th smallest element in array A
    inputs are:
    A: array
    k: index
    f: function
    I: initial value
    depth: depth of recursion"""
    indent = "  " * depth # indentation for debugging


    if len(A) == 0:
        return None
    elif k < 0 or k >= len(A):
        return None
    elif len(A) == 1:
        result = A[0]
        return result

    # Step 1: Select pivot
    p = selectPivot(A, depth)
    print(f'{indent}selectPivot: Selected pivot {p} from array {A}')

    # Step 2: Filter elements less than pivot

    from filter2 import filter
    L = filter(A, lambda x: x < p, f, I, depth+1)
    print(f'{indent}filter: Filtered elements less than pivot {p} from array {A}')

    # Step 3: Filter elements greater than pivot
    G = filter(A, lambda x: x > p, f, I, depth+1)
    print(f'{indent}filter: Filtered elements greater than pivot {p} from array {A}')

    # Step 4: Determine which case we are in

    # Elements equal to pivot: len(A) - len(L) - len(G)
    # These would be positioned after all elements < p and before elements > p
    equal_count = len(A) - len(L) - len(G)
    print(f'{indent}equal_count: {equal_count}')

    # Case 1: k is smaller than |L|, so answer is in L
    if k < len(L):
        result = kthSmallest(L, k, f, I, depth+1)
    # Case 2: k is within the range of pivot elements, so answer is the pivot
    elif k < len(L) + equal_count:
        result = p
    # Case 3: k is larger than all pivot elements, so answer is in G
    else:
        new_k = k - len(L) - equal_count
        result = kthSmallest(G, new_k, f, I, depth+1)

    return result


if __name__ == "__main__":
    '''
    # Test cases
    test_arrays = [
        [3, 1, 4, 1, 5, 9, 2, 6],  # Mixed order with duplicates
        [10, 7, 8, 9, 1, 5],       # Unsorted array
        [1, 2, 3, 4, 5],           # Already sorted
        [5, 4, 3, 2, 1],           # Reverse sorted
        [42],                       # Single element
    ]

    def add(x, y):
        return x + y


    for i, arr in enumerate(test_arrays):

        # Test various k values
        for k in range(len(arr)):
            result = kthSmallest(arr, k, add, 0)

            # Verify result by sorting
            sorted_arr = sorted(arr)
            expected = sorted_arr[k]
            assert result == expected, f"Error: expected {expected}, got {result}"

'''
    # test only with one array
    test_arrays = [
        [3, 1, 4, 1, 5, 9, 2, 6],  # Mixed order with duplicates
    ]

    def add(x, y):
        return x + y

    for i, arr in enumerate(test_arrays):
        for k in range(len(arr)):
            result = kthSmallest(arr, k, add, 0)
            sorted_arr = sorted(arr)
            expected = sorted_arr[k]
            assert result == expected, f"Error: expected {expected}, got {result}"

