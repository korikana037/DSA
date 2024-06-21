class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        temp = ''
        for i in s:
            if i != ' ':
                temp += i
            elif temp != '':
                result.append(temp)
                temp = ''
        if temp != '':
            result.append(temp)

        return ' '.join(result[::-1])


# Time complexity : O(n) for traversing the string and n is the length of the input string
# Space complexity : O(n) space required to store the result string