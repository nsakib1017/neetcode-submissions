class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        count = {}
        left = 0

        for i in s1:
            count[i] = count.get(i,0)+1

        have, need = 0, len(count)
        if len(s1) > len(s2):
            return False
        
        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1

            if s2[right] in count and count[s2[right]] == window[s2[right]]:
                have+=1
            while (right-left+1) > len(s1):
                if s2[left] in count and count[s2[left]] == window[s2[left]]:
                    have-=1
                window[s2[left]]-=1
                left+=1
            if have==need:
                return True
        return False

            
