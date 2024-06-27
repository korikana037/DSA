class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        #time complexity is O(n^2) and space complexity is O(1)
        i=0
        j=i+1
        a = True
        while a:
            if nums[i]+nums[j]==target:
                return [i,j]
            else:
                j+=1
            if j == len(nums):
                i +=1
                j = i+1
        # time complexity is O(n) and space complexity is O(1)