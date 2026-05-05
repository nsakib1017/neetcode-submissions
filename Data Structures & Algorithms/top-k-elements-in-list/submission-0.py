class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for num in nums:
            if num_dict.get(num):
                num_dict[num] = num_dict[num]+1
            else:
                num_dict[num] = 1

        num_dict_sorted = dict(sorted(num_dict.items(), key=lambda item: item[1], reverse=True))
        list_top_k = list(num_dict_sorted.keys())
        return list_top_k[:k]