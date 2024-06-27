# can be solved in 3 ways
# 1. using sorting algorithims
# 2. using hashmaps or counting
# 3. dutch partition algorithm

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ones, zeroes, n = 0, 0, len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes += 1
            elif nums[i] == 1:
                ones += 1
        for i in range(zeroes):
            nums[i] = 0
        for i in range(zeroes, zeroes+ones):
            nums[i]= 1
        for i in range(zeroes+ones, n):
            nums[i] =2

# time complexity is O(n) and space complexity is O(1)


# dutch partition alogoruthm :
# The Dutch National Flag problem was proposed by Edsger Dijkstra. It is a classic algorithm
# for sorting an array containing three distinct values, often represented as low, mid, and high.
# The goal is to partition the array into three sections: one containing all elements less than
# a certain value (low), one containing elements equal to that value (mid), and one containing
# elements greater than that value (high). The algorithm typically uses three pointers to achieve
# this partitioning in a single pass with linear time complexity O(n) and constant space complexity
# O(1).

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low ,mid = 0,0
        high = len(nums)-1
        while mid<=high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1