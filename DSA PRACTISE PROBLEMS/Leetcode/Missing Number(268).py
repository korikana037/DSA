class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i
        #n = len(nums)
        # expected_sum = n*(n+1)//2
        # actual_sum = sum(nums)
        # return expected_sum-actual_sum

        #using xor
        n = len(nums)+1
        xor_all = 0
        for i in range(n):
            xor_all ^= i
        for num in nums:
            xor_all ^= num
        return xor_all
 # time complexity is (n)
 # space complexity is O(1)