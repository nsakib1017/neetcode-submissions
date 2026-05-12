class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        charSet = set()
        res = 0

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res


