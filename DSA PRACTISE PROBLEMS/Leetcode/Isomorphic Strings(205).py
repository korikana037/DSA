class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashs = {}
        hasht = {}
        for s1, t1 in zip(s, t):
            if s1 in hashs and hashs[s1] != t1:
                return False
            else:
                hashs[s1] = t1

            if t1 in hasht and hasht[t1] != s1:
                return False
            else:
                hasht[t1] = s1
        return True

# time complexity is O(n)
# space complexity is

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_chars = {}
        set_vals = set()
        for i in range(len(s)):
            if s[i] in map_chars:
                if map_chars[s[i]] != t[i]:
                    return False
            else:
                if t[i] in set_vals:
                    return False
                map_chars[s[i]] = t[i]
                set_vals.add(t[i])
        return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s))==len(set(t))==len(set(zip(s,t)))