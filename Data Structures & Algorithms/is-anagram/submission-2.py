class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = {}
        sorted_t = {}

        for c in s:
            if c not in sorted_s:
                sorted_s[c] = 1
            else:
                sorted_s[c] += 1
        for c in t:
            if c not in sorted_t:
                sorted_t[c] = 1
            else:
                sorted_t[c] += 1
        return sorted_s == sorted_t