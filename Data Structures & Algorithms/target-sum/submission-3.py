class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def helper(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            return helper(i+1, total + nums[i]) + helper(i+1, total-nums[i])
        return helper(0, 0)