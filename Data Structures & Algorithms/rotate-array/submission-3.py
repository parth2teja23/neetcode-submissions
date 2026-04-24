class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            n = len(nums)
            temp = nums[n-1]
            nums.pop(n-1)
            nums.insert(0, temp)
        