class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def helper(i ,total, subset):
            if total == target:
                res.append(subset.copy())
                return
            if total > target:
                return
            if i >= len(candidates):
                return

            subset.append(candidates[i])
            helper(i+1, total + candidates[i], subset)
            subset.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            helper(i+1, total, subset)
        
        res = []
        helper(0, 0, [])
        return res