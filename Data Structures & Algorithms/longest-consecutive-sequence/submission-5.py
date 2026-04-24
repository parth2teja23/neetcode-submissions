class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        maxLen = 0
        for i in mySet:
            if i-1 not in mySet:
                length = 1
                while (i+length) in mySet:
                    length += 1
                maxLen = max(maxLen, length)
        return maxLen
