def plusScan(sizes, f, I, depth=0):

    # Use the scan function from scan2.py to calculate prefix sums
    from scan2 import scan
    X, total = scan(sizes, f, I)
    return X, total


def flatten(A, f, I, depth=0):

    # Step 1: Calculate sizes of each sub-list
    n = len(A)
    sizes = [None] * n

    for i in range(n):
        sizes[i] = len(A[i])


    # Step 2: Calculate starting positions using plus scan
    X, m = plusScan(sizes, f, I, depth+1)

    # Step 3: Create result array
    R = [None] * m

    # Step 4: Copy elements using double loop
    for i in range(n):
        o = X[i]
        sublist = A[i]

        for j in range(len(sublist)):
            R[o + j] = A[i][j]

    return R


if __name__ == "__main__":
    nested_array = [[10, 20], [30], [40, 50]]
    def add(x, y): return x + y
    flattened = flatten(nested_array, add, 0)
