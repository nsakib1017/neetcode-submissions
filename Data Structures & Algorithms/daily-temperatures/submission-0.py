class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result_stack = [0] * len(temperatures)
        stack_temp = []

        for i, temp in enumerate(temperatures):
            while stack_temp and temp > stack_temp[-1][0]:
                stackTemp, stackIdx = stack_temp.pop()
                result_stack[stackIdx] = i-stackIdx
            stack_temp.append((temp, i))
        return result_stack