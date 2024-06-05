
# Write a function to find the missing number in a given integer array of 1 to 100.
# The function takes to parameter the array and the number of elements that needs to be in array.
# For example if we want to find missing number from 1 to 6 the second parameter will be 6.

def missing_number(arr, n):
    for i in range(n-1):
        if arr[i] != arr[i+1]-1:
            return arr[i]+1

def missing_num(arr, n):
    expected_sum = n*(n+1)//2
    actual_sum = sum(arr)
    missing_num = expected_sum - actual_sum
    return missing_num

arr=[1,2,3,4,6]
print(missing_number(arr, 6))
print(missing_num(arr, 6))
