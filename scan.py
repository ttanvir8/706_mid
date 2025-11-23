def scanUp(A, L, f, depth=0):
    print(f'\n%%%%%%%%%%%%%%% inside scanUp: A={A}, L={L}, depth={depth}')
    if len(A) == 1:
        print(f"A has one element: {A[0]}. Returning A[0].")
        return A[0]
    n = len(A)
    m = n // 2
    print(
        f"Splitting A into left A[0:{m}]={A[:m]} and right A[{m}:{n}]={A[m:]}")
    l = scanUp(A[:m], L[:m-1], f, depth+1)
    r = scanUp(A[m:], L[m-1:], f, depth+1)
    L[m-1] = l
    print(f"Set L[{m-1}] = {l}")
    result = f(l, r)
    print(f"Returning f({l}, {r}) = {result}")
    return result


def scanDown(R, L, f, s, depth=0):
    print(
        f'\n%%%%%%%%%%%%%%% inside scanDown: R={R}, L={L}, s={s}, depth={depth}')
    if len(R) == 1:
        R[0] = s
        print(f"R has one element. Setting R[0] = {s}")
        return
    n = len(R)
    m = n // 2
    print(
        f"Splitting R into left R[0:{m}]={R[:m]} and right R[{m}:{n}]={R[m:]}")
    scanDown(R[:m], L[:m-1], f, s, depth+1)
    scanDown(R[m:], L[m-1:], f, f(s, L[m-1]), depth+1)
    print(f"scanDown done for depth={depth}")


def scan(A, f, I):
    print(f'\n############## scan start')
    n = len(A)
    L = [None] * (n - 1)
    R = [None] * n
    print(f"Initial array: {A}")
    total = scanUp(A, L, f)
    print(f"scanUp complete. L={L}, total={total}")
    scanDown(R, L, f, I)
    print(f"scanDown complete. R={R}")
    return R, total


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    def add(x, y): return x + y
    prefix_sums, total = scan(arr, add, 0)
    print(f"Prefix sums: {prefix_sums}")
    print(f"Total sum: {total}")
