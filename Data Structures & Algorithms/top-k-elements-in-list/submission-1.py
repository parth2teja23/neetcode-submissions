class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        topk = []

        for num in count.keys():
            heapq.heappush(topk, (count[num], num))
            if len(topk) > k:
                heapq.heappop(topk)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(topk)[1])

        return res