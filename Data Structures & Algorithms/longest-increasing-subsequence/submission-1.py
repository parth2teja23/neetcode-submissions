class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, j): # i -> cur index , j -> last included index
            if i == len(nums):
                return 0
            LIS = dfs(i+1, j) # to skip
            
            if j == -1 or nums[i] > nums[j]:
                LIS = max(LIS,1 + dfs(i + 1, i)) # to include


            return LIS
        return dfs(0, -1)