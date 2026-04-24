class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n+1) for _ in range(n)]
        def helper(i, prev):
            if i == len(nums):
                return 0

            if dp[i][prev-1] != -1:
                return dp[i][prev-1]
            
            res = helper(i+1, prev)
            if prev == -1 or nums[prev] < nums[i]:
                res = max(res, 1 + helper(i+1, i))
            return res
        
            dp[i][prev-1] = res
        
        return helper(0, -1)