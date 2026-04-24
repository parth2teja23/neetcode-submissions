class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def helper(i, total, subset):
            if i >= len(nums):
                return
            if total > target:
                return 
            if total == target:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            helper(i, total + nums[i], subset)
            subset.pop()
            helper(i+1, total, subset)
            
        helper(0,0, subset)
        return res