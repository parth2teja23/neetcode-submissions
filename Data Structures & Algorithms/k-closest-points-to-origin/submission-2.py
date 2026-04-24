class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minH = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = (x**2) + (y**2)
            heapq.heappush(minH, [-dist, x, y])
            if len(minH) > k:
                heapq.heappop(minH)
        heapq.heapify(minH)
        res = []
        for point in minH:
            res.append([point[1], point[2]])
        return res
