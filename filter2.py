def plusScan(flags, f, I, depth=0):
    indent = "  " * depth
    print(f'\n{indent}-> plusScan: flags={flags}, depth={depth}')

    # Use the scan function from scan2.py to calculate prefix sums
    from scan2 import scan
    X, m = scan(flags, f, I)
    print(f'{indent}<- plusScan: Returning X: {X}, m: {m}')
    return X, m


def filter(A, p, f, I, depth=0):
    indent = "  " * depth

    print(f'\n{indent}======== FILTER START =========')
    print(f'{indent}Input array: {A}')
    print(f'{indent}Predicate function: {p}')

    # Step 1: Get the size of input array
    n = len(A)
    print(f'{indent}Step 1: n = |A| = {n}')

    # Step 2: Create flag array F to store predicate results
    F = [None] * n
    print(f'\n{indent}Step 2: Creating flag array F of size {n}: {F}')

    # Step 3: Calculate predicate for each element (parfor simulation)
    print(f'\n{indent}Step 3: Computing predicate results for each element:')
    for i in range(n):
        result = p(A[i])
        F[i] = 1 if result else 0
        print(f'{indent}  F[{i}] = p(A[{i}]) = p({A[i]}) = {result} -> {F[i]}')

    print(f'\n{indent}Completed flag array: F = {F}')

    # Step 4: Calculate destination indices using plus scan
    print(f'\n{indent}Step 4: Computing destination indices using plus scan:')
    X, m = plusScan(F, f, I, depth+1)
    print(f'{indent}Scan complete: X = {X}, total surviving elements m = {m}')

    # Step 5: Create result array R with size m
    R = [None] * m
    print(f'\n{indent}Step 5: Creating result array R of size {m}: {R}')

    # Step 6: Copy surviving elements to result array (parfor simulation)
    print(f'\n{indent}Step 6: Copying surviving elements to result array:')
    for i in range(n):
        if F[i]:
            dest_index = X[i]
            R[dest_index] = A[i]
            print(
                f'{indent}  F[{i}] = {F[i]}, copying A[{i}] = {A[i]} to R[{dest_index}]')
        else:
            print(f'{indent}  F[{i}] = {F[i]}, skipping A[{i}] = {A[i]}')

    print(f'\n{indent}======== FILTER COMPLETE ========')
    print(f'{indent}Final result: R = {R}')
    return R


if __name__ == "__main__":
    # Test the filter function
    array = [1, 2, 3, 4, 5, 6]

    # Define predicate functions
    def is_even(x):
        return x % 2 == 0

    def is_greater_than_3(x):
        return x > 3

    def add(x, y):
        return x + y

    print("Testing filter with even numbers:")
    even_numbers = filter(array, is_even, add, 0)
    print(f"Even numbers: {even_numbers}")

    print("\n" + "="*50)
    print("Testing filter with numbers greater than 3:")
    greater_than_3 = filter(array, is_greater_than_3, add, 0)
    print(f"Numbers > 3: {greater_than_3}")
