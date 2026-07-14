class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return sorted([i, j])
        # return []
        seen = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen:
                return [seen[difference], i]
            seen[nums[i]] = i
        return[]