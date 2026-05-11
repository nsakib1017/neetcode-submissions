class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        l=0
        res = 1
        freqMap = {}

        for r in range(len(s)):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)
            maxF = max(maxF, freqMap.get(s[r]))

            while (r-l+1) - maxF > k:
                freqMap[s[l]] -= 1
                l+=1
            
            res = max(res, r-l+1)
        return res