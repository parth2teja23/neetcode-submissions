class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def helper(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            
            if i >= len(candidates):
                return
            
            if total > target:
                return
            
            subset.append(candidates[i])
            helper(i+1, subset, total + candidates[i])
            subset.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            helper(i + 1, subset, total)
        
        helper(0, [], 0)
        return res