def plusScan(sizes, f, I, depth=0):
    print(f'\n%%%%%%%%%%%%%%% inside plusScan: sizes={sizes}, depth={depth}')

    # Use the scan function from scan2.py to calculate prefix sums
    from scan2 import scan
    X, total = scan(sizes, f, I)
    print(f"Returning X: {X}, total: {total}")
    return X, total


def flatten(A, f, I, depth=0):
    print(f'\n############## flatten start')
    print(f"Input nested array: {A}")

    # Step 1: Calculate sizes of each sub-list
    n = len(A)
    print(f"n = |A| = {n}")
    sizes = [None] * n
    print(f"sizes = [None] * {n} = {sizes}")
    print(f"\n%%%%%%%%%%%%%%% Calculating sizes:")

    for i in range(n):
        sizes[i] = len(A[i])
        print(f"sizes[{i}] = |A[{i}]| = {sizes[i]}")

    print(f"sizes = {sizes}")

    # Step 2: Calculate starting positions using plus scan
    X, m = plusScan(sizes, f, I, depth+1)
    print(f"Starting positions X = {X}")
    print(f"Total size m = {m}")

    # Step 3: Create result array
    R = [None] * m
    print(f"Created result array R of size {m}: {R}")

    # Step 4: Copy elements using double loop
    print(f"\n%%%%%%%%%%%%%%% Copying elements:")
    for i in range(n):
        o = X[i]
        sublist = A[i]
        print(f"Processing sub-list {i}: {sublist}, offset o = {o}")

        for j in range(len(sublist)):
            print(f"when j={j}, o={o}, R[o + j] = (o{o} + j{j}) = {o + j}")
            R[o + j] = A[i][j]
            print(f"  R[{o + j}] = A[{i}][{j}] = {A[i][j]}")

    print(f"Flatten complete. R = {R}")
    return R


if __name__ == "__main__":
    nested_array = [[10, 20], [30], [40, 50]]
    def add(x, y): return x + y
    flattened = flatten(nested_array, add, 0)
    print(f"Final result: {flattened}")
