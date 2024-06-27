class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            last = nums[-1]
            for j in range(len(nums) - 1, 0, -1):
                nums[j] = nums[j - 1]
            nums[0] = last

## codewise correct but time limit exceeds in case of larger arays


## for right rotation
# first reverse the whole array, then revesre the first k elements and then reverse the next
#k+1 to last element
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        L = len(nums)
        if L == k: return

        k = k%L # the case when k > L
        nums.reverse()

        for i in range(k//2):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]

        for i in range(k, (L+k)//2):
            nums[i], nums[L-1-i+k] = nums[L-1-i+k], nums[i]

## time complexity is O(n)
#space complexity is O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            a=nums.pop()
            nums.insert(0,a)
#time complexity is o(n2)
#space complexity is o(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

#time complexity is O(n)
# space complexity is O(n)