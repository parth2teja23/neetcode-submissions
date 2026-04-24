class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        maxP = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                p = prices[j] - prices[i]
                maxP = max(p, maxP)
        return maxP