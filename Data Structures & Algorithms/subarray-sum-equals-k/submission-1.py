class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curSum = 0
        seen = { 0: 1 }
        for i in range(len(nums)):
            curSum += nums[i]
            count += seen.get(curSum-k , 0)
            seen[curSum] = seen.get(curSum, 0) + 1
        return count