def findBlock(A, v, k, start=0, end=None, depth=0):
    if end is None:
        end = len(A)


    n = end - start
    s = n // k
    r = k


    # Check k positions evenly spaced out
    for i in range(k):
        left_idx = start + i * s
        right_idx = start + (i + 1) * s

        # Ensure we don't go out of bounds
        if right_idx > end:
            right_idx = end


        # Check if value belongs in this block (between left boundary and next boundary)
        if (left_idx < end and A[left_idx] <= v and
                (right_idx >= end or A[right_idx] > v)):
            r = i
            break

    block_start = start + r * s
    block_end = start + (r + 1) * s
    if block_end > end:
        block_end = end

    return A[block_start:block_end], block_start


def search(A, v, k, start=0, end=None, depth=0):
    if end is None:
        end = len(A)


    # Find the block that contains the value
    B, o = findBlock(A, v, k, start, end, depth+1)

    # Base case: if the block is small enough, we're done
    if len(B) <= k:
        return o
    else:
        # Recursive case: search within the smaller block
        result = search(A, v, k, o, o + len(B), depth+1)
        return result


if __name__ == "__main__":
    # Test with a sorted array
    sorted_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    value_to_find = 65
    k = 3  # Number of splits/processors

    position = search(sorted_array, value_to_find, k)

    # Test edge cases

    # Test finding existing value
    position2 = search(sorted_array, 50, k)

    # Test finding value at beginning
    position3 = search(sorted_array, 10, k)

    # Test finding value at end
    position4 = search(sorted_array, 100, k)

    # Test with smaller k value for more recursion
    position5 = search(sorted_array, 75, k=2)
