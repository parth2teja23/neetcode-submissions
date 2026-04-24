class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minH = nums
        heapq.heapify(minH)
        while len(minH) > k:
            heapq.heappop(minH)
        return heapq.heappop(minH)