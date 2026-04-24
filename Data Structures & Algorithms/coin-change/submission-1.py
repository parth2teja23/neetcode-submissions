class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def helper(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + helper(amount-coin))
            dp[amount] = res
            return res

        minCoins = helper(amount)
        if minCoins >= 1e9:
            return -1
        else:
            return minCoins
