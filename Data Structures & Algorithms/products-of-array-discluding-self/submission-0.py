class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_output = 1
        count_zero = 0
        for num in nums:
            if num:
                total_output = total_output * num
            else:
                count_zero = count_zero + 1 
        result = []

        if count_zero > 1:
            return [0 for i in range(0, len(nums))]
        elif count_zero == 1:
            return [total_output if i == 0 else 0 for i in nums]
        else:
            return [total_output // i for i in nums]




        