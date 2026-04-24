class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxH = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = (x**2) + (y**2)
            heapq.heappush(maxH, [-dist, x, y])
            if len(maxH) > k:
                heapq.heappop(maxH)
        heapq.heapify(maxH)
        res = []
        for point in maxH:
            res.append([point[1], point[2]])
        return res
