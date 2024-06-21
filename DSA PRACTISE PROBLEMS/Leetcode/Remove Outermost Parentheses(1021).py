

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        result = ''
        first = 0
        for i in range(len(s)):
            if s[i] == "(":
                count += 1
            if s[i] == ')':
                count -= 1
            if count == 0:
                result += s[first+1:i]
                first = i+1
        return result

# Time Complexity: O(n), where n is the length of the input string S.
# Space Complexity: O(n), primarily due to the space required to store the result string res

# second method with same time and space complexity

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        popen, result = 0, []
        for x in S:
            if x==')':
                popen -= 1
            if popen>0:
                result.append(x)
            if x=='(':
                popen += 1
        return ''.join(result)