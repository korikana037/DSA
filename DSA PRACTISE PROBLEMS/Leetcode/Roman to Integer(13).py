class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):  # Changed <= to <
            if s[i] == 'M':
                result += 1000
                i += 1
            elif s[i] == 'D':
                result += 500
                i += 1
            elif s[i] == 'C':
                if i + 1 < len(s) and s[i + 1] == 'M':
                    result += 900
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == 'D':
                    result += 400
                    i += 2
                else:
                    result += 100
                    i += 1
            elif s[i] == 'L':
                result += 50
                i += 1
            elif s[i] == 'X':
                if i + 1 < len(s) and s[i + 1] == 'C':
                    result += 90
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == 'L':
                    result += 40
                    i += 2
                else:
                    result += 10
                    i += 1
            elif s[i] == 'V':
                result += 5
                i += 1
            elif s[i] == 'I':
                if i + 1 < len(s) and s[i + 1] == 'X':
                    result += 9
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == 'V':
                    result += 4
                    i += 2
                else:
                    result += 1
                    i += 1
        return result


class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0

        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i + 1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]

        return ans

# Time complexity is O(n)
# space complexity is O(1)

#integer to roman conversion:
class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the value-symbol pairs in descending order
        val_to_sym = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        # Initialize the result string
        roman = ""

        # Convert the integer to Roman numeral
        for value, symbol in val_to_sym:
            while num >= value:
                roman += symbol
                num -= value

        return roman
