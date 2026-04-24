class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        K = k % len(nums)
        def ulta(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        ulta(nums, 0, len(nums)-1)
        ulta(nums, 0, K-1)
        ulta(nums, K, len(nums)-1)
        