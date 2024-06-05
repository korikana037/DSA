# Find max product of two integers in an array where alla the elements are positive

def max_product1(arr):
    max_product = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]*arr[j] > max_product:
                max_product = arr[i]*arr[j]
    return max_product


def max_product2(arr):
    i = 0
    j = i + 1
    max_product = 0
    while i < len(arr) - 1:
        if arr[i] * arr[j] > max_product:
            max_product = arr[i] * arr[j]
        j += 1

        if j == len(arr):
            i += 1
            j = i + 1
    return max_product


def max_product3(arr):
    max1, max2 = 0, 0
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max1*max2


arr = [1, 7, 3, 4, 9, 5]

print(max_product1(arr))
print(max_product2(arr))
print(max_product3(arr))

