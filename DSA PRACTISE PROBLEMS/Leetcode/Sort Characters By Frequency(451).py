class Solution:
    def frequencySort(self, s: str) -> str:
        seen = {}
        key_list =[]
        for i in s:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        sorted_seen = {k:v for k,v in sorted(seen.items(), key=lambda item: item[1], reverse = True)}
        for key, value in sorted_seen.items():
            for i in range(value):
                key_list.append(key)
        return "".join(key_list)

# time complexity is O(nlogn) and space complexity is O(n)