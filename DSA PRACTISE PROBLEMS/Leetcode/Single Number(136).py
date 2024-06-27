class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i] = 1
        for key in seen:
            if seen[key] == 1:
                return key

# time complexity is o(n)
# space complexity is O(n)
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor
# time complexity is O(n)
# space complexity is O(1)