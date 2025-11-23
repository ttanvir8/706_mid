def findBlock(A, v, k, start=0, end=None, depth=0):
    if end is None:
        end = len(A)

    print(
        f'\n%%%%%%%%%%%%%%% inside findBlock: A={A[start:end]}, v={v}, k={k}, start={start}, end={end}, depth={depth}')

    n = end - start
    print(f"end - start = {end} - {start} = {n}")
    print(f"Array size n = {n}")
    s = n // k
    print(f"Block size s = {s}")
    r = k
    print(f"Initial r = {r}")

    # Check k positions evenly spaced out
    for i in range(k):
        left_idx = start + i * s
        print(f"when i={i}, start={start}, s={s}, left_idx = (srart{start} + i{i} * s{s}) = {left_idx}")
        right_idx = start + (i + 1) * s
        print(f"when i={i}, s={s}, right_idx = (start{start} + (i{i} + 1) * s{s}) = {right_idx}")

        # Ensure we don't go out of bounds
        if right_idx > end:
            right_idx = end

        print(
            f"  Checking block {i}: A[{left_idx}:{right_idx}] = {A[left_idx:right_idx]}")

        # Check if value belongs in this block (between left boundary and next boundary)
        if (left_idx < end and A[left_idx] <= v and
                (right_idx >= end or A[right_idx] > v)):
            r = i
            print(f"  Found block {i} contains v={v}")
            break

    block_start = start + r * s
    block_end = start + (r + 1) * s
    if block_end > end:
        block_end = end

    print(
        f"Returning block A[{block_start}:{block_end}] = {A[block_start:block_end]}, offset = {block_start}")
    return A[block_start:block_end], block_start


def search(A, v, k, start=0, end=None, depth=0):
    '''
    inputs are:
    A: array
    v: value to search
    k: number of splits
    start: start index
    end: end index
    depth: depth of recursion
    '''
    if end is None:
        end = len(A)

    print(
        f'\n############## search start: A={A[start:end]}, v={v}, k={k}, start={start}, end={end}, depth={depth}')

    # Find the block that contains the value
    B, o = findBlock(A, v, k, start, end, depth+1)
    print(f"Found block B={B}, offset o={o}")

    # Base case: if the block is small enough, we're done
    if len(B) <= k:
        print(f"Base case reached: |B|={len(B)} <= k={k}")
        print(f"Value {v} belongs at position {o} (start of block)")
        return o
    else:
        # Recursive case: search within the smaller block
        print(f"Recursive case: |B|={len(B)} > k={k}, searching in block")
        result = search(A, v, k, o, o + len(B), depth+1)
        print(f"Recursive search returned {result}")
        return result


if __name__ == "__main__":
    # Test with a sorted array
    sorted_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    value_to_find = 65
    k = 3  # Number of splits/processors

    print(f"Searching for value {value_to_find} in array {sorted_array}")
    print(f"Using k={k} splits")

    position = search(sorted_array, value_to_find, k)
    print(f"Value {value_to_find} belongs at position {position}")
'''
    # Test edge cases
    print("\n" + "="*50)
    print("Testing edge cases:")

    # Test finding existing value
    position2 = search(sorted_array, 50, k)
    print(f"Value 50 belongs at position {position2}")

    # Test finding value at beginning
    position3 = search(sorted_array, 10, k)
    print(f"Value 10 belongs at position {position3}")

    # Test finding value at end
    position4 = search(sorted_array, 100, k)
    print(f"Value 100 belongs at position {position4}")

    # Test with smaller k value for more recursion
    print("\n" + "="*50)
    print("Testing with k=2 for more recursion:")
    position5 = search(sorted_array, 75, k=2)
    print(f"Value 75 with k=2 belongs at position {position5}")

'''