class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_map = {}
        for i, val in enumerate(nums):
            dict_map[val]=i
        for i, val in enumerate(nums):
            k = target - val
            if dict_map.get(k) and i != dict_map.get(k):
                return [i, dict_map.get(k)]
        