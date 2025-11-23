def calculate_sizes(A, depth=0):
    print(f'\n%%%%%%%%%%%%%%% inside calculate_sizes: A={A}, depth={depth}')
    sizes = []
    for i, sublist in enumerate(A):
        size = len(sublist)
        sizes.append(size)
        print(f"Sub-list {i}: {sublist} has size {size}")
    print(f"Returning sizes: {sizes}")
    return sizes


def plus_scan(sizes, depth=0):
    print(f'\n%%%%%%%%%%%%%%% inside plus_scan: sizes={sizes}, depth={depth}')
    n = len(sizes)
    X = [0] * n
    total = 0

    for i in range(n):
        X[i] = total
        total += sizes[i]
        print(f"X[{i}] = {X[i]}, total = {total}")

    print(f"Returning X: {X}, total: {total}")
    return X, total


def flatten_array(A, depth=0):
    print(f'\n############## flatten_array start')
    print(f"Input nested array: {A}")

    # Step 1: Calculate sizes of each sub-list
    sizes = calculate_sizes(A, depth+1)

    # Step 2: Calculate starting positions using plus scan
    X, total_size = plus_scan(sizes, depth+1)
    print(f"Starting positions: {X}")
    print(f"Total size: {total_size}")

    # Step 3: Create result array
    R = [None] * total_size
    print(f"Created result array R of size {total_size}: {R}")

    # Step 4: Copy elements using double loop
    print(f"\n%%%%%%%%%%%%%%% Copying elements:")
    for i in range(len(A)):
        sublist = A[i]
        offset = X[i]
        print(f"Processing sub-list {i}: {sublist}, offset = {offset}")

        for j in range(len(sublist)):
            R[offset + j] = sublist[j]
            print(f"  R[{offset + j}] = A[{i}][{j}] = {sublist[j]}")

    print(f"Flatten complete. R = {R}")
    return R


if __name__ == "__main__":
    nested_array = [[10, 20], [30], [40, 50]]
    flattened = flatten_array(nested_array)
    print(f"Final result: {flattened}")
