import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ansList = []
        heap = []

        for i in range(k):
            heapq.heappush(heap, (-1*nums[i], i))

        ansList.append(-1*heap[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(heap, (-1*nums[i], i))

            while heap and heap[0][1] <= i-k:
                heapq.heappop(heap)

            ansList.append(-1*heap[0][0])

        return ansList