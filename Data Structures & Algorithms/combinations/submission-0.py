class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(i, subset):
            if len(subset) == k:
                res.append(subset.copy())
                return
            if i > n:
                return
            
            for j in range(i, n+1):
                subset.append(j)
                helper(j+1, subset)
                subset.pop()
        
        helper(1, [])
        return res
            