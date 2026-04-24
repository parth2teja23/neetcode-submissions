class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def helper(amount):
            if amount == 0:
                return 0
            res = float("inf")

            if amount in dp:
                return dp[amount]

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + helper(amount-coin))
            dp[amount] = res
            return res

    
        mincoins = helper(amount)
        return -1 if mincoins == float("inf") else mincoins