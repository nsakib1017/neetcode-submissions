class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>=2:
            largest = -heapq.heappop(stones)
            second_largest = -heapq.heappop(stones)

            if largest != second_largest:
                heapq.heappush(stones, -1*(largest-second_largest))
        return  -1 * heapq.heappop(stones) if stones else 0