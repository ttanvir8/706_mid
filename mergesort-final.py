def merge(l, r):
    print(f'\n%%%%%%%%%%%%%%%inside merge left={l} and right={r}')
    if not l:
        print(f"l is no, left={l}, return right {r}")
        return r
    if not r:
        print(f"r is no, return left={l}, right={r}")
        return l
    if l[0] <= r[0]:
        print(
            f"#####compare first element of l={l[0]} with first right element r={r[0]}, L0 is smaller")
        print(
            f"it return L0={[l[0]]} and merge rest of left={l[1:]} with right {r}")
        return [l[0]] + merge(l[1:], r)
    else:
        print(
            f">>>>compare first element of l={l[0]} with first right element r={r[0]}, R0 is smaller")
        print(
            f"it returns {[r[0]]} and merge left={l} with rest of right {r[1:]}")
        return [r[0]] + merge(l, r[1:])


def sort(arr):
    print('############## sort start')
    count = 1
    print(f"this is = {count}")
    print(arr)
    if len(arr) <= 1:
        print(f"nothing and length={len(arr)}, {arr}")
        return arr

    mid = len(arr) // 2
    l = arr[:mid]
    r = arr[mid:]
    l = sort(l)
    r = sort(r)
    count = count + 1
    print('############## sort done')
    return merge(l, r)


arr = [2, 3, 45, 1, 4, 6, 5, 44, 67, 88]
sort(arr)
