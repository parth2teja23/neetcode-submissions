class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def helper(subset, mask):
            if len(subset) == n:
                res.append(subset.copy())
                return
            
            for i in range(n):
                if mask & (1 << i):
                    continue
                subset.append(nums[i])
                helper(subset, mask | (1 << i))
                subset.pop()
        
        helper([], 0)
        return res
