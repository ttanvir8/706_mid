import random


def selectPivot(A, depth=0):
    """Select a pivot element from array A"""
    indent = "  " * depth

    if len(A) == 0:
        print(f'{indent}selectPivot: Empty array, returning None')
        return None
    elif len(A) == 1:
        pivot = A[0]
        print(f'{indent}selectPivot: Single element array, returning {pivot}')
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

        print(f'{indent}selectPivot: Selected pivot {pivot} from array {A}')
        return pivot


def kthSmallest(A, k, f, I, depth=0):
    """Find the k-th smallest element in array A"""
    indent = "  " * depth

    print(f'\n{indent}======== KTH SMALLEST START =========')
    print(f'{indent}Input array: {A}')
    print(f'{indent}Looking for k-th smallest where k = {k}')

    if len(A) == 0:
        print(f'{indent}ERROR: Empty array!')
        return None
    elif k < 0 or k >= len(A):
        print(f'{indent}ERROR: k={k} is out of bounds for array size {len(A)}')
        return None
    elif len(A) == 1:
        result = A[0]
        print(f'{indent}Base case: Single element array, k-th smallest is {result}')
        print(f'{indent}======== KTH SMALLEST COMPLETE ========')
        return result

    # Step 1: Select pivot
    print(f'\n{indent}Step 1: Selecting pivot')
    p = selectPivot(A, depth)

    # Step 2: Filter elements less than pivot
    print(f'\n{indent}Step 2: Filtering elements less than pivot')
    print(f'{indent}Filter condition: x < {p}')

    from filter2 import filter
    L = filter(A, lambda x: x < p, f, I, depth+1)
    print(f'{indent}Elements less than {p}: {L}')

    # Step 3: Filter elements greater than pivot
    print(f'\n{indent}Step 3: Filtering elements greater than pivot')
    print(f'{indent}Filter condition: x > {p}')
    G = filter(A, lambda x: x > p, f, I, depth+1)
    print(f'{indent}Elements greater than {p}: {G}')

    # Step 4: Determine which case we are in
    print(f'\n{indent}Step 4: Decision logic')
    print(f'{indent}Array size: |A| = {len(A)}')
    print(f'{indent}L size: |L| = {len(L)}')
    print(f'{indent}G size: |G| = {len(G)}')
    print(f'{indent}k = {k}')

    # Elements equal to pivot: len(A) - len(L) - len(G)
    # These would be positioned after all elements < p and before elements > p
    equal_count = len(A) - len(L) - len(G)
    print(f'{indent}Elements equal to pivot: {equal_count}')
    print(f'{indent}First position of elements equal to pivot: {len(L)}')
    print(f'{indent}Last position of elements equal to pivot: {len(L) + equal_count - 1}')

    # Case 1: k is smaller than |L|, so answer is in L
    if k < len(L):
        print(f'\n{indent}Case 1: k ({k}) < |L| ({len(L)})')
        print(f'{indent}The {k}-th smallest element is in the "less than" group')
        print(f'{indent}Recursively searching in L for k-th smallest')
        result = kthSmallest(L, k, f, I, depth+1)
        print(f'{indent}Result from L: {result}')
    # Case 2: k is within the range of pivot elements, so answer is the pivot
    elif k < len(L) + equal_count:
        print(f'\n{indent}Case 2: {len(L)} <= k ({k}) < {len(L) + equal_count}')
        print(f'{indent}The {k}-th smallest element is the pivot: {p}')
        print(f'{indent}(k is within the range of elements equal to pivot)')
        result = p
    # Case 3: k is larger than all pivot elements, so answer is in G
    else:
        new_k = k - len(L) - equal_count
        print(f'\n{indent}Case 3: k ({k}) >= {len(L) + equal_count}')
        print(f'{indent}The {k}-th smallest element is in the "greater than" group')
        print(f'{indent}New k = {k} - {len(L)} - {equal_count} = {new_k}')
        print(f'{indent}Recursively searching in G for {new_k}-th smallest')
        result = kthSmallest(G, new_k, f, I, depth+1)
        print(f'{indent}Result from G: {result}')

    print(f'\n{indent}======== KTH SMALLEST COMPLETE ========')
    print(f'{indent}Final result: {result}')
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

    print("Testing kthSmallest algorithm:")

    for i, arr in enumerate(test_arrays):
        print(f"\n{'='*60}")
        print(f"Test Case {i+1}: {arr}")

        # Test various k values
        for k in range(len(arr)):
            print(f"\n--- Finding {k}-th smallest ---")
            result = kthSmallest(arr, k, add, 0)
            print(f"Result: {result}")

            # Verify result by sorting
            sorted_arr = sorted(arr)
            expected = sorted_arr[k]
            print(f"Expected: {expected} (from sorted array: {sorted_arr})")
            assert result == expected, f"Error: expected {expected}, got {result}"

        print(f"✓ All tests passed for array: {arr}")

    print(f"\n{'='*60}")
    print("All test cases completed successfully!")
'''
    test_arrays = [
        [3, 1, 4, 1, 5, 9, 2, 6],  # Mixed order with duplicates
    ]

    def add(x, y):
        return x + y

    arr = test_arrays[0]
    k = 2
    result = kthSmallest(arr, k, add, 0)
    sorted_arr = sorted(arr)
    expected = sorted_arr[k]
    print(f"Result: {result}")
'''
    for i, arr in enumerate(test_arrays):
        for k in range(len(arr)):
            result = kthSmallest(arr, k, add, 0)
            sorted_arr = sorted(arr)
            expected = sorted_arr[k]
            print(f"Result: {result}")
            #print(f"Expected: {expected} (from sorted array: {sorted_arr})")
            #assert result == expected, f"Error: expected {expected}, got {result}"
'''
    
