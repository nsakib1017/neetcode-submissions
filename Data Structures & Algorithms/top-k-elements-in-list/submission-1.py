class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = {}
        for num in nums:
            count_nums[num] = 1 + count_nums.get(num, 0)
        
        heap = []

        for num in count_nums.keys():
            heapq.heappush(heap, (count_nums[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res