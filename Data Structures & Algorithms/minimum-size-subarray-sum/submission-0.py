class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sum = 0
        length = 0
        minLen = float('inf')
        for r in range(len(nums)):
            sum += nums[r]
            length = r-l+1
            while sum >= target:
                minLen = min(length, minLen) 
                sum -= nums[l]
                l += 1
                length -= 1
        return minLen if minLen != float('inf') else 0