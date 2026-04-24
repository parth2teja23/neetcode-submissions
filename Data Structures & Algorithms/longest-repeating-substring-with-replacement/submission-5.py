class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        length = 0
        mostFreq = 0
        maxLen = 0
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            mostFreq = max(mostFreq, window[s[r]])

            while (r-l+1) - mostFreq > k:
                window[s[l]] -= 1
                l += 1
            maxLen = max(r-l+1, maxLen)
        return maxLen
