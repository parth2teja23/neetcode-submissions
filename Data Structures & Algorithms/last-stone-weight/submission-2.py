class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # minHeap = stones
        # heapq.heapify(minHeap)
        # while len(minHeap) > 1:
        #     first = heapq.heappop(minHeap)
        #     sec = heapq.heappop(minHeap)
        #     diff = max(first, sec) - min(first, sec)
        #     heapq.heappush(minHeap, diff)
        # return minHeap[0]

        maxH = [-s for s in stones]
        heapq.heapify(maxH)
        while len(maxH) > 1:
            first = heapq.heappop(maxH)
            sec = heapq.heappop(maxH)
            if first == sec:
                continue
            else:
                diff = first - sec
                heapq.heappush(maxH, diff)
        return -maxH[0] if maxH else 0
