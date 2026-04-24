class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for mask in range(1 << n):       # 0 to 2^n - 1
            skip = False
            subset = []

            for i in range(n):
                if mask & (1 << i):      # bit i is set → include nums[i]
                    # if nums[i] == nums[i-1] but left bit not set → duplicate
                    if i > 0 and nums[i] == nums[i-1] and not (mask & (1 << (i-1))):
                        skip = True
                        break
                    subset.append(nums[i])

            if not skip:
                result.append(subset)

        return result