class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]

        return ""

# Time complexity = o(n)
# space complexity : O(1)

# Note : here dont convert the whole string to integer and then divide by 2, just convert the
# the single digit into into and findout whether it is odd or even. coz you may encounter error
#while converting large string into integer, which exceeds the efault limit of string to
# integer conversion in python