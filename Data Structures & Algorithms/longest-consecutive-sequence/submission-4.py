class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        length = 1
        maxLen = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i+1] - nums[i] == 1:
                length += 1
                maxLen = max(length, maxLen)
            else:
                length = 1

        return maxLen 