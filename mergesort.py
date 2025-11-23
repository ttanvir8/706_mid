# MergeSort in Python (recursive divide-and-conquer approach)

print("=== MERGE SORT DEBUG OUTPUT ===")
print("Starting recursive merge sort algorithm...")


def merge_sort(arr, depth=0, position="main"):
    """Recursive merge sort with detailed debug output"""
    indent = "  " * depth
    print(f"{indent}=== RECURSIVE CALL: depth={depth}, position='{position}' ===")
    print(f"{indent}Line 8: Input array: {arr}")

    # Base case: if array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        print(f"{indent}Line 11: Base case reached: array length = {len(arr)} <= 1")
        print(f"{indent}Line 12: Returning sorted array: {arr}")
        return arr

    # Divide step: split array into two halves
    print(f"{indent}=== DIVIDE STEP ===")
    mid = len(arr) // 2
    print(f"{indent}Line 16: mid = len(arr) // 2 = {len(arr)} // 2 = {mid}")

    print(f"{indent}Line 17: Dividing array into left and right halves")
    left_half = arr[:mid]
    print(f"{indent}Line 18: Left half: {left_half}")
    right_half = arr[mid:]
    print(f"{indent}Line 19: Right half: {right_half}")

    # Conquer step: recursively sort both halves
    print(f"{indent}=== CONQUER STEP: Recursive calls ===")
    print(f"{indent}Line 22: Recursively sorting left half...")
    left_sorted = merge_sort(left_half, depth + 1, "left")
    print(f"{indent}Line 23: Left half sorted result: {left_sorted}")

    print(f"{indent}Line 25: Recursively sorting right half...")
    right_sorted = merge_sort(right_half, depth + 1, "right")
    print(f"{indent}Line 26: Right half sorted result: {right_sorted}")

    # Merge step: combine the sorted halves
    print(f"{indent}=== MERGE STEP ===")
    print(f"{indent}Line 29: Merging sorted halves: {left_sorted} and {right_sorted}")
    merged = merge(left_sorted, right_sorted, depth)
    print(f"{indent}Line 30: Merged result: {merged}")
    print(f"{indent}Line 31: Returning merged array from depth {depth}")
    return merged


def merge(left, right, depth=0):
    """Merge two sorted arrays with detailed debug output"""
    indent = "  " * depth
    print(f"{indent}=== MERGE FUNCTION: depth={depth} ===")
    print(f"{indent}Line 35: Merging left: {left} and right: {right}")

    merged = []
    print(f"{indent}Line 37: Created empty merged array: {merged}")

    i = j = 0
    print(f"{indent}Line 39: i = {i}, j = {j}")

    print(f"{indent}Line 40: Starting while loop: i < len(left) ({i} < {len(left)}) and j < len(right) ({j} < {len(right)})")
    while i < len(left) and j < len(right):
        print(
            f"{indent}  Comparing left[{i}] = {left[i]} with right[{j}] = {right[j]}")
        if left[i] < right[j]:
            print(
                f"{indent}  Line 42: {left[i]} < {right[j]}, appending {left[i]} to merged")
            merged.append(left[i])
            print(f"{indent}  Line 43: merged = {merged}")
            i += 1
            print(f"{indent}  Line 43: i incremented to {i}")
        else:
            print(
                f"{indent}  Line 45: {right[j]} <= {left[i]}, appending {right[j]} to merged")
            merged.append(right[j])
            print(f"{indent}  Line 46: merged = {merged}")
            j += 1
            print(f"{indent}  Line 46: j incremented to {j}")

    # Append remaining elements from left array
    print(f"{indent}Line 48: Checking for remaining elements in left: i < len(left) ({i} < {len(left)})")
    while i < len(left):
        print(
            f"{indent}  Line 49: Appending remaining left[{i}] = {left[i]} to merged")
        merged.append(left[i])
        print(f"{indent}  Line 50: merged = {merged}")
        i += 1
        print(f"{indent}  Line 50: i incremented to {i}")

    # Append remaining elements from right array
    print(f"{indent}Line 52: Checking for remaining elements in right: j < len(right) ({j} < {len(right)})")
    while j < len(right):
        print(
            f"{indent}  Line 53: Appending remaining right[{j}] = {right[j]} to merged")
        merged.append(right[j])
        print(f"{indent}  Line 54: merged = {merged}")
        j += 1
        print(f"{indent}  Line 54: j incremented to {j}")

    print(f"{indent}Line 56: Merge complete, returning: {merged}")
    return merged


# Driver code
print("\n=== MAIN EXECUTION ===")
print("Line 60: Starting main execution")
array = [6, 5, 12, 10, 9, 1]
print(f"Line 61: Initial array: {array}")

print("\nLine 62: Calling merge_sort function...")
sorted_array = merge_sort(array)
print(f"\nLine 63: Sorting complete!")
print(f"Line 64: Final sorted array: {sorted_array}")

print("\n=== FINAL RESULT ===")
print("Sorted array is:")
for v in sorted_array:
    print(v, end=" ")
print()
