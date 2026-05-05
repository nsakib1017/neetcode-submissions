class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        curr = 0

        for num in nums:
            if num-1 not in num_set:
                curr_length = 1
                curr = num
                while True:
                    curr = curr + 1
                    if curr in num_set:
                        curr_length = curr_length + 1
                    else:
                        break
            
                max_length = max(max_length, curr_length)
        return max_length




        