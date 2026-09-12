class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        freqMap = {}
        l=0

        for r in range(len(s)):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)
            maxF = max(maxF, freqMap[s[r]])

            while (r-l+1) - maxF > k:
                freqMap[s[l]] -=1
                l+=1
            res = max(maxF, r-l+1)
        return res