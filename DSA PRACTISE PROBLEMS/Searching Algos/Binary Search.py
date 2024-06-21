def Binary_search(arr, low, high, target):
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return -1


def recursive_binary_search(arr, low, high, target):
    if high >= low:
        mid = low + (high-low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return recursive_binary_search(arr, mid+1, high, target)
        else:
            return recursive_binary_search(arr, low, mid-1, target)

    return -1


