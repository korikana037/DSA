class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                result = max(count, result)
            else:
                count = 0
        return result

# time complexity is O(n)
# space complexity is O(10)