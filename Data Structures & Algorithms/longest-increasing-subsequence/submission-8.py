class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def helper(i, prev):
            if i >= len(nums):
                return 0

                
            take = 0
            if (i, prev) in dp:
                return dp[(i, prev)]
            skip = helper(i+1, prev)


            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + helper(i+1, i)

            dp[(i, prev)] = max(take, skip)
            return dp[(i, prev)]
        return helper(0, -1)