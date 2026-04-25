class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = {}
        def helper(i, remaining):
            if i >= len(coins):
                return MAX
            if remaining < 0:
                return MAX
            
            if remaining == 0:
                return 0
            
            if (i, remaining) in dp:
                return dp[(i, remaining)]
                

            
            take = 1 + helper(i, remaining-coins[i])
            noTake = helper(i+1, remaining)
            dp[(i, remaining)] = min(take, noTake)
            return dp[(i, remaining)]
        
        res = helper(0, amount)
        return res if res != MAX else -1

