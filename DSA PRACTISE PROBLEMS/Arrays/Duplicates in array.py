# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.


def contains_duplicate(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]==nums[j]:
                return True

def contains_duplicate2(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(contains_duplicate(nums))
print(contains_duplicate2(nums))