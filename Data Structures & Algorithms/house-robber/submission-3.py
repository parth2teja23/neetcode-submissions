class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)
        def helper(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(helper(i+1) , nums[i] + helper(i+2))
            return dp[i]
        return max(helper(0), helper(2))