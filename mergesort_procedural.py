# MergeSort in Python (bottom-up iterative procedure, no functions)

print("=== MERGE SORT DEBUG OUTPUT ===")
print("Starting merge sort algorithm...")

# Driver input: the array to sort
print("Line 4: Initializing array with values [6, 5, 12, 10, 9, 1]")
array = [6, 5, 12, 10, 9, 1]
print(f"Line 5: Array initialized: {array}")
n = len(array)
print(f"Line 6: Array length n = {n}")

print("\n=== DIVIDE AND CONQUER PHASE ===")
print("Starting bottom-up iterative merge sort...")

# Bottom-up iterative merge sort (procedural, no function definitions)
print("Line 9: Initializing width = 1")
width = 1
print(f"Line 10: Starting main while loop: width = {width}, n = {n}")
while width < n:
    print(f"\n--- DIVIDE STEP: Processing subarrays of width = {width} ---")
    print(f"Line 11: Array state before processing: {array}")

    # For each pair of subarrays of size `width`
    print(f"Line 12: Starting for loop with left in range(0, {n}, {2*width})")
    for left in range(0, n, 2*width):
        print(f"\n  Processing subarray pair starting at left = {left}")
        mid = min(left + width, n)
        print(f"  Line 13: mid = min({left} + {width}, {n}) = {mid}")
        right = min(left + 2*width, n)
        print(f"  Line 14: right = min({left} + {2*width}, {n}) = {right}")

        # Merge array[left:mid] and array[mid:right] into a temporary list
        print(
            f"  Line 15: Merging subarrays array[{left}:{mid}] and array[{mid}:{right}]")
        print(f"  Line 15: Left subarray: {array[left:mid]}")
        print(f"  Line 15: Right subarray: {array[mid:right]}")

        merged = []
        print(f"  Line 16: Created empty merged list: {merged}")
        i = left
        print(f"  Line 17: i = left = {i}")
        j = mid
        print(f"  Line 18: j = mid = {j}")

        print(
            f"  Line 19: Starting while loop: i < mid ({i} < {mid}) and j < right ({j} < {right})")
        while i < mid and j < right:
            print(
                f"    Comparing array[{i}] = {array[i]} with array[{j}] = {array[j]}")
            if array[i] < array[j]:
                print(
                    f"    Line 20: {array[i]} < {array[j]}, so appending {array[i]} to merged")
                merged.append(array[i])
                print(f"    Line 21: merged = {merged}")
                i += 1
                print(f"    Line 21: i incremented to {i}")
            else:
                print(
                    f"    Line 23: {array[j]} <= {array[i]}, so appending {array[j]} to merged")
                merged.append(array[j])
                print(f"    Line 24: merged = {merged}")
                j += 1
                print(f"    Line 24: j incremented to {j}")

        # Append any remaining elements from the left half
        print(
            f"  Line 26: Checking for remaining elements in left half: i < mid ({i} < {mid})")
        while i < mid:
            print(
                f"    Line 27: Appending remaining element array[{i}] = {array[i]} to merged")
            merged.append(array[i])
            print(f"    Line 28: merged = {merged}")
            i += 1
            print(f"    Line 28: i incremented to {i}")

        # Append any remaining elements from the right half
        print(
            f"  Line 30: Checking for remaining elements in right half: j < right ({j} < {right})")
        while j < right:
            print(
                f"    Line 31: Appending remaining element array[{j}] = {array[j]} to merged")
            merged.append(array[j])
            print(f"    Line 32: merged = {merged}")
            j += 1
            print(f"    Line 32: j incremented to {j}")

        # Write merged back into the original array
        print(
            f"  Line 34: Writing merged result {merged} back to array[{left}:{right}]")
        array[left:right] = merged
        print(f"  Line 34: Array after merge: {array}")

    # Increase the subarray size
    print(f"\n--- CONQUER STEP COMPLETED for width = {width} ---")
    print(f"Line 36: Array state after width={width} pass: {array}")
    width *= 2
    print(f"Line 37: width multiplied by 2, now width = {width}")

print("\n=== MERGE SORT COMPLETED ===")
print(f"Final sorted array: {array}")

# Print the sorted array
print("\nSorted array is:")
for v in array:
    print(v, end=" ")
print()
