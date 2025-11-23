# MergeSort in Python (bottom-up iterative procedure, no functions)

print("=== MERGE SORT DEBUG OUTPUT ===")
print("Starting merge sort algorithm...")

# Driver input: get array from user
print("Line 4: Prompting user for input")
print("Enter numbers separated by spaces:")
input_string = input()
print(f"Line 5: User input received: '{input_string}'")
array = [int(x) for x in input_string.split()]
print(f"Line 6: Converted input to array: {array}")
n = len(array)
print(f"Line 7: Array length n = {n}")

print("\n=== DIVIDE AND CONQUER PHASE ===")
print("Starting bottom-up iterative merge sort...")

# Bottom-up iterative merge sort (procedural, no function definitions)
print("Line 10: Initializing width = 1")
width = 1
print(f"Line 11: Starting main while loop: width = {width}, n = {n}")
while width < n:
    print(f"\n--- DIVIDE STEP: Processing subarrays of width = {width} ---")
    print(f"Line 12: Array state before processing: {array}")

    # For each pair of subarrays of size `width`
    print(f"Line 13: Starting for loop with left in range(0, {n}, {2*width})")
    for left in range(0, n, 2*width):
        print(f"\n  Processing subarray pair starting at left = {left}")
        mid = min(left + width, n)
        print(f"  Line 14: mid = min({left} + {width}, {n}) = {mid}")
        right = min(left + 2*width, n)
        print(f"  Line 15: right = min({left} + {2*width}, {n}) = {right}")

        # Merge array[left:mid] and array[mid:right] into a temporary list
        print(
            f"  Line 16: Merging subarrays array[{left}:{mid}] and array[{mid}:{right}]")
        print(f"  Line 16: Left subarray: {array[left:mid]}")
        print(f"  Line 16: Right subarray: {array[mid:right]}")

        merged = []
        print(f"  Line 17: Created empty merged list: {merged}")
        i = left
        print(f"  Line 18: i = left = {i}")
        j = mid
        print(f"  Line 19: j = mid = {j}")

        print(
            f"  Line 20: Starting while loop: i < mid ({i} < {mid}) and j < right ({j} < {right})")
        while i < mid and j < right:
            print(
                f"    Comparing array[{i}] = {array[i]} with array[{j}] = {array[j]}")
            if array[i] < array[j]:
                print(
                    f"    Line 21: {array[i]} < {array[j]}, so appending {array[i]} to merged")
                merged.append(array[i])
                print(f"    Line 22: merged = {merged}")
                i += 1
                print(f"    Line 22: i incremented to {i}")
            else:
                print(
                    f"    Line 24: {array[j]} <= {array[i]}, so appending {array[j]} to merged")
                merged.append(array[j])
                print(f"    Line 25: merged = {merged}")
                j += 1
                print(f"    Line 25: j incremented to {j}")

        # Append any remaining elements from the left half
        print(
            f"  Line 27: Checking for remaining elements in left half: i < mid ({i} < {mid})")
        while i < mid:
            print(
                f"    Line 28: Appending remaining element array[{i}] = {array[i]} to merged")
            merged.append(array[i])
            print(f"    Line 29: merged = {merged}")
            i += 1
            print(f"    Line 29: i incremented to {i}")

        # Append any remaining elements from the right half
        print(
            f"  Line 31: Checking for remaining elements in right half: j < right ({j} < {right})")
        while j < right:
            print(
                f"    Line 32: Appending remaining element array[{j}] = {array[j]} to merged")
            merged.append(array[j])
            print(f"    Line 33: merged = {merged}")
            j += 1
            print(f"    Line 33: j incremented to {j}")

        # Write merged back into the original array
        print(
            f"  Line 35: Writing merged result {merged} back to array[{left}:{right}]")
        array[left:right] = merged
        print(f"  Line 35: Array after merge: {array}")

    # Increase the subarray size
    print(f"\n--- CONQUER STEP COMPLETED for width = {width} ---")
    print(f"Line 37: Array state after width={width} pass: {array}")
    width *= 2
    print(f"Line 38: width multiplied by 2, now width = {width}")

print("\n=== MERGE SORT COMPLETED ===")
print(f"Final sorted array: {array}")

# Print the sorted array
print("\nSorted array is:")
for v in array:
    print(v, end=" ")
print()
