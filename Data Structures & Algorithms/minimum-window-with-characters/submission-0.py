class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        res = [-1, -1]

        resLen = 1000000

        if t == "":
            return ""
        
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        for l in range(len(s)):
            countS = {}
            for r in range(l, len(s)):
                countS[s[r]] = 1 + countS.get(s[r], 0)
                flag = True

                for c in countT:
                    if countT[c] > countS.get(c,0):
                        flag = False
                        break
                
                if flag and (r-l+1) < resLen:
                    resLen =  r-l+1
                    res = [l,r]
        
        l,r = res
        
        return s[l : r+1] if resLen != 1000000 else ""
