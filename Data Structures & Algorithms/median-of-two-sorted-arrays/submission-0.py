class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1 + nums2
        res.sort()
        n = len(res)
        if n % 2 == 1:
            return res[n//2]
        else:
            return (res[(n//2)-1] + res[n//2]) / 2