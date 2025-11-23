def scanUp(A, L, f, start=0, end=None, depth=0):
    if end is None:
        end = len(A)

    indent = "  " * depth
    print(
        f'\n{indent}-> scanUp: A={A[start:end]}, L={L[start:end-1] if end-start > 1 else []}, depth={depth}')

    if end - start == 1:
        print(
            f'{indent}  Base case: A has one element: {A[start]}. Returning A[start].')
        return A[start]
    else:
        n = end - start
        m = n // 2
        mid = start + m
        print(f'{indent}  Splitting A[{start}:{end}] into:')
        print(f'{indent}    Left A[{start}:{mid}] = {A[start:mid]}')
        print(f'{indent}    Right A[{mid}:{end}] = {A[mid:end]}')

        print(f'{indent}  Recursively processing left half...')
        l = scanUp(A, L, f, start, mid, depth+1)
        print(f'{indent}  Left result: {l}')

        print(f'{indent}  Recursively processing right half...')
        r = scanUp(A, L, f, mid, end, depth+1)
        print(f'{indent}  Right result: {r}')

        if mid - 1 < len(L):
            L[mid - 1] = l
            print(f'{indent}  Store L[{mid-1}] = {l}')

        result = f(l, r)
        print(f'{indent}  Combine: f({l}, {r}) = {result}')
        print(f'{indent}<- scanUp: Returning {result}')
        return result


def scanDown(R, L, f, s, start=0, end=None, depth=0):
    if end is None:
        end = len(R)

    indent = "  " * depth
    print(
        f'\n{indent}-> scanDown: R={R[start:end]}, L={L[start:end-1] if end-start > 1 else []}, s={s}, depth={depth}')

    if end - start == 1:
        R[start] = s
        print(
            f'{indent}  Base case: R has one element. Setting R[{start}] = {s}')
        print(f'{indent}<- scanDown: Completed depth {depth}')
        return
    else:
        n = end - start
        m = n // 2
        mid = start + m
        print(f'{indent}  Splitting R[{start}:{end}] into:')
        print(f'{indent}    Left R[{start}:{mid}] = {R[start:mid]}')
        print(f'{indent}    Right R[{mid}:{end}] = {R[mid:end]}')

        print(f'{indent}  Processing left half with s = {s}...')
        scanDown(R, L, f, s, start, mid, depth+1)

        if mid - 1 < len(L) and L[mid - 1] is not None:
            new_s = f(s, L[mid - 1])
            print(
                f'{indent}  Processing right half with s = f({s}, L[{mid-1}]) = f({s}, {L[mid-1]}) = {new_s}...')
            scanDown(R, L, f, new_s, mid, end, depth+1)
        else:
            print(
                f'{indent}  Processing right half with s = {s} (no intermediate result)...')
            scanDown(R, L, f, s, mid, end, depth+1)

        print(f'{indent}<- scanDown: Completed depth {depth}')


def scan(A, f, I):
    indent = ""

    print(f'\n{indent}======== SCAN START =========')
    n = len(A)
    L = [None] * (n - 1)
    R = [None] * n
    print(f'{indent}Input array: {A}')
    print(f'{indent}Creating auxiliary arrays: L (size {n-1}), R (size {n})')

    print(f'\n{indent}Phase 1: Upward phase (computing prefix sums)')
    total = scanUp(A, L, f)
    print(f'{indent}Upward phase complete:')
    print(f'{indent}  L = {L}')
    print(f'{indent}  Total = {total}')

    print(f'\n{indent}Phase 2: Downward phase (distributing results)')
    scanDown(R, L, f, I)
    print(f'{indent}Downward phase complete: R = {R}')
    print(f'\n{indent}======== SCAN COMPLETE =========')
    return R, total


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    def add(x, y): return x + y
    prefix_sums, total = scan(arr, add, 0)
    print(f"\nFinal results:")
    print(f"Prefix sums: {prefix_sums}")
    print(f"Total sum: {total}")
