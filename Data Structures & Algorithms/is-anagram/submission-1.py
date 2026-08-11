class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for c in s:
            if c not in count_s:
                count_s[c] = 1
            else:
                count_s[c] += 1
        
        for d in t:
            if d not in count_t:
                count_t[d] = 1
            else:
                count_t[d] += 1
        
        return count_s == count_t