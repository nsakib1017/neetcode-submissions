class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map = {}
        windowMap = {}

        for c in s1:
            s1Map[c] = 1 + s1Map.get(c, 0)

        l = 0
        have = 0
        need = len(s1Map)

        for r in range(len(s2)):
            c = s2[r]
            windowMap[c] = 1 + windowMap.get(c, 0)
            if c in s1Map and windowMap[c] == s1Map[c]:
                have += 1

            while r - l + 1 > len(s1):
                if s2[l] in s1Map and windowMap[s2[l]] == s1Map[s2[l]]:
                    have -= 1
                windowMap[s2[l]] -= 1

                l += 1

            if have == need:
                return True

        return False