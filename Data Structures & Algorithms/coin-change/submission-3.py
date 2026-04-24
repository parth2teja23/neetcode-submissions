class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def helper(amount):
            if amount == 0:
                return 0

            if amount in dp:
                return dp[amount]

            res = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res,1 + helper(amount - coin))
                dp[amount] = res
            
            return res

        minCoins = helper(amount)
        return -1 if minCoins == float("inf") else minCoins