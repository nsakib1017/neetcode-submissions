class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l=0
        hashMap, windowMap = {}, {}

        for c in s1:
            hashMap[c] = 1 + hashMap.get(c, 0)
        have,need=0,len(hashMap)

        for r in range(len(s2)):
            windowMap[s2[r]] = 1 + windowMap.get(s2[r], 0)

            if s2[r] in hashMap and windowMap[s2[r]] == hashMap[s2[r]]:
                have+=1
            
            while (r-l+1) > len(s1):
                if s2[l] in hashMap and windowMap[s2[l]] == hashMap[s2[l]]:
                    have-=1
                windowMap[s2[l]]-=1
                l+=1
            if need==have:
                return True
        return False
