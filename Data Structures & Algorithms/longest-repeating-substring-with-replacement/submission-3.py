class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        maxLen = 0
        l = 0
        freq = {}
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            while (r-l+1) - max(freq.values()) > k:
                freq[s[l]] -=1
                l += 1
            maxLen = max(maxLen, r-l+1)
        return maxLen

