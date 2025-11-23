def scanUp(A, L, f, start=0, end=None, depth=0):
    if end is None:
        end = len(A)

    indent = "  " * depth

    if end - start == 1:
        return A[start]
    else:
        n = end - start
        m = n // 2
        mid = start + m

        l = scanUp(A, L, f, start, mid, depth+1)

        r = scanUp(A, L, f, mid, end, depth+1)

        if mid - 1 < len(L):
            L[mid - 1] = l

        result = f(l, r)
        return result


def scanDown(R, L, f, s, start=0, end=None, depth=0):
    if end is None:
        end = len(R)

    indent = "  " * depth

    if end - start == 1:
        R[start] = s
        return
    else:
        n = end - start
        m = n // 2
        mid = start + m

        scanDown(R, L, f, s, start, mid, depth+1)

        if mid - 1 < len(L) and L[mid - 1] is not None:
            new_s = f(s, L[mid - 1])
            scanDown(R, L, f, new_s, mid, end, depth+1)
        else:
            scanDown(R, L, f, s, mid, end, depth+1)


def scan(A, f, I):
    indent = ""

    n = len(A)
    L = [None] * (n - 1)
    R = [None] * n

    total = scanUp(A, L, f)

    scanDown(R, L, f, I)
    return R, total


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    def add(x, y): return x + y
    prefix_sums, total = scan(arr, add, 0)
