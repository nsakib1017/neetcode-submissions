class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=curr=ans=0
        for right in range(len(prices)):
            profit = prices[right]-prices[left]
            while profit < 0:
                left+=1
                profit = prices[right]-prices[left]
            ans = max(ans, profit)
        return ans