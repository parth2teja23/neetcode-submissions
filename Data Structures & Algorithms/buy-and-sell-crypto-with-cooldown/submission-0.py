class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # key -> (i, buy) value -> maxprofit
        def helper(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                buy = helper(i+1, not buying) - prices[i]
                cooldown = helper(i+1, buying)
                dp[(i, buying)] =  max(buy, cooldown)
            else:
                sell = helper(i+2, not buying) + prices[i]
                cooldown = helper(i+1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]


        return helper(0, True)