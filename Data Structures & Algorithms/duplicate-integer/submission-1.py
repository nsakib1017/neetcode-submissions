class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for x in nums:
            num_dict[x] = 0
        for x in nums:
            num_dict[x] = num_dict[x]+1
        for x in num_dict.keys():
            if num_dict[x] > 1:
                return True
        return False
           