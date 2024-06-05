# Write a function called middle that takes a list and returns a new list that contains all
# but the first and last elements.

def middle1(nums):
    nums.pop(0)
    nums.pop(-1)
    return nums


def middle2(nums2):
    return nums2[1:-1]


nums = [1, 2, 3, 4, 5, 6]
nums2 = [1, 2, 3, 4]
print(middle1(nums))
print(middle2(nums2))
