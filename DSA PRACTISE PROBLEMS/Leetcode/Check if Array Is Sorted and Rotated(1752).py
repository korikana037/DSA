class Solution:
    def check(self, nums: List[int]) -> bool:
        def checking(nums):
            for i in range(1,len(nums)):
                if nums[i]<nums[i-1]:
                    return False
            return True

        for i in range(len(nums)):
            if checking(nums):
                return True
            else:
                nums = nums[1:]+nums[:1]
        return False

# Time complexity : O(n^2)
# checking fun takes O(n) time compexity.
# Each rotation operation takes O(n) time due to slicing.
#In each iteration of the outer loop, the checking function is called, which takes O(n) time.
#Each iteration also involves a rotation operation, which takes O(n) time.
#Therefore, each iteration of the outer loop takes O(n)+O(n)=O(n) time.
#Since there are up to n iterations, the total time complexity is O(n^2)

# space complexity: o(n) Each rotation creates a new array using slicing, which takes O(n) space.
# However, since we're using a new array at each step, the space complexity remains O(n).

    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)):
            if nums[i - 1] > nums[i]:
                count += 1
        return count <= 1
#time complexity is O(n) and space complexity is O(1)
# rotating an array after sorting will only have one break point. so count the numebr of
#break points and reurn the answer. true if no of breakpoitns is 0 or 1 orelse false