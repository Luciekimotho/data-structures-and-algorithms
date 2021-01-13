def search(arr, start, stop, key):
    mid = start + ((stop - start) // 2)

    if start > stop:
        return -1

    if key == arr[mid]:
        return mid
    elif key < arr[mid]:
        return search(arr, start, mid-1, key)
    else:
        return search(arr, mid+1, stop, key)

arr = [1, 10, 20, 47, 59, 63, 75]
key = 1
n = len(arr)

print(search(arr, 0, n-1, key))


def search2(arr, key):
    start = 0
    stop = len(arr) - 1

    while start <= stop:
        mid = start + ((stop - start) // 2)
        if key == arr[mid]:
            return mid
        if key < arr[mid]:
            stop = mid-1
        else:
            start = mid+1
    return -1


print(search2(arr, key))