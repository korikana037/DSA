class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=0
        for i in range(1,len(nums)):
            if nums[a]!=nums[i]:
                nums[a+1] = nums[i]
                a+=1
        return a+1

# time complexity is O(n)
# space complexity is O(1)