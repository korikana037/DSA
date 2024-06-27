class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=-1
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break
        if j == -1:
            return nums
        k = j+1
        while k<len(nums):
            if nums[k] != 0:
                nums[j], nums[k] = nums[k], nums[j]
                k+=1
                j+=1
            else:
                k+=1
#time complixity is O(n)
#space complexity is O(1)


def moveZeros(n: int, a: [int]) -> [int]:
    temp = []
    for i in range(n):
        if a[i] != 0:
            temp.append(a[i])
    nz = len(temp)
    for i in range(nz):
        a[i] = temp[i]

    for i in range(nz, n):
        a[i] = 0
    return a

#time complexity is o(n)
#space complexity is O(n)

def moveZeroes(self, nums):
    n = len(nums)
    i = 0
    for j in range(n):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

#






