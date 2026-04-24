class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set()
        for word in wordDict:
            wordSet.add(word)
        n = len(s)
        dp = [-1] * (n+1)
        def helper(i):
            if i == len(s):
                return True
            if dp[i] != -1:
                return dp[i]
            for j in range(i+1, n+1):
                
                if s[i:j] in wordSet:
                    dp[i] = True
                    if helper(j):
                        return True
            dp[i] = False
            return False

        return helper(0)