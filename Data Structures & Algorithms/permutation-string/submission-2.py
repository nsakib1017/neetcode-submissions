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

            if r - l + 1 > len(s1):
                left_char = s2[l]

                if left_char in s1Map and windowMap[left_char] == s1Map[left_char]:
                    have -= 1

                windowMap[left_char] -= 1

                # if windowMap[left_char] == 0:
                #     del windowMap[left_char]

                l += 1

            if have == need:
                return True

        return False