class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text2) + 1
        m = len(text1) + 1
        dp = [[-1] * n for _ in range(m)]
        def helper(i,j):

            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + helper(i+1, j+1)

            if dp[i][j] != -1:
                return dp[i][j]

            word1next = helper(i+1, j)
            word2next = helper(i, j+1)
            dp[i][j] = max(word1next, word2next)
            return dp[i][j]
        return helper(0,0)