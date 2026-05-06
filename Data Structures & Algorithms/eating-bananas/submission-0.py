class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r

        while l <= r:
            totalTime = 0
            mid = l + (r-l) // 2
            for p in piles:
                totalTime += math.ceil(float(p)/mid)
            if totalTime > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        return res