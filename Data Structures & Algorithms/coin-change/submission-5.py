class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        res = MAX
        dp = {}
        def helper(index, remaining):
            
            if remaining == 0:
                return 0  
            if remaining < 0:
                return MAX 
            if index == len(coins):
                return MAX 

            if (index, remaining) in dp:
                return dp[(index, remaining)]
            
            take = 1 + helper(index, remaining - coins[index])
            
            noTake = helper(index + 1, remaining)
            
            dp[(index, remaining)] = min(take, noTake)
            return dp[(index, remaining)]
        
        result = helper(0, amount)
        return result if result != MAX else -1  # Return -1 if impossible