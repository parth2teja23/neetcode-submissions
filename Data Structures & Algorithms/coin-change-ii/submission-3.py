class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = {}
        def helper(i, remaining):
            if i >= len(coins):
                return 0
            if remaining < 0:
                return 0
            
            if remaining == 0:
                return 1

            if (i, remaining) in dp:
                return dp[(i, remaining)]
            
            take = helper(i, remaining - coins[i])
            noTake = helper(i+1, remaining)
            dp[(i, remaining)] = take + noTake
            return dp[(i, remaining)]
        
        return helper(0, amount)
        