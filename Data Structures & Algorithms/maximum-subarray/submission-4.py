class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            if sum < 0:
                sum = 0
            sum += nums[i]
            maxSum = max(sum, maxSum)
            
        return maxSum
