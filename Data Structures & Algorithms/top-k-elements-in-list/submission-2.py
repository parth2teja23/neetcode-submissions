class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))
        while len(heap) > k:
            heapq.heappop(heap)

        res = []
        for i in heap:
            res.append(i[1])
        return res