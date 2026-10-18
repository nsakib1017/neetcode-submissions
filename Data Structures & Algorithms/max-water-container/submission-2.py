class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        marea = float("-inf")
        while left <= right:
            area = min(heights[left], heights[right]) * (right-left)
            marea = max(marea, area)

            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
        return marea
