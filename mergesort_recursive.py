# MergeSort in Python


def mergeRecursive(L, M, array, i, j, k):
    # Base case: if we've exhausted either L or M, return current positions
    if i >= len(L) or j >= len(M):
        return i, j, k

    # Recursive case: compare elements and place the smaller one
    if L[i] < M[j]:
        array[k] = L[i]
        return mergeRecursive(L, M, array, i + 1, j, k + 1)
    else:
        array[k] = M[j]
        return mergeRecursive(L, M, array, i, j + 1, k + 1)


def mergeRemaining(L, array, i, k):
    # Base case: if we've exhausted L, return current positions
    if i >= len(L):
        return i, k

    # Recursive case: place remaining elements from L
    array[k] = L[i]
    return mergeRemaining(L, array, i + 1, k + 1)


def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        # Merge the sorted halves using recursive approach
        i, j, k = mergeRecursive(L, M, array, 0, 0, 0)

        # Merge remaining elements from L if any
        i, k = mergeRemaining(L, array, i, k)

        # Merge remaining elements from M if any
        j, k = mergeRemaining(M, array, j, k)


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)
