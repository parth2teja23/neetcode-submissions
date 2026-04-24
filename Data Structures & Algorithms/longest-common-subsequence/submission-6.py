class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) 
        n = len(text2) 
        dp = [[-1] * n for _ in range(m)]
        def helper(i, j):
            if i >= m or j >= n:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = 1 + helper(i+1, j+1)
                return dp[i][j]
            else:
                moveword1 = helper(i+1, j)
                moveword2 = helper(i, j+1)
                dp[i][j] = max(moveword1, moveword2)
                return dp[i][j]
        return helper(0,0)
