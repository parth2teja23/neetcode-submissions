class CountSquares:

    def __init__(self):
        self.pointCount = defaultdict(int)
        self.graph = []

    def add(self, point: List[int]) -> None:
        self.pointCount[tuple(point)] += 1
        self.graph.append(point)

    def count(self, point: List[int]) -> int:
        count = 0
        x = point[0]
        y = point[1]
        for p in self.graph:
            px = p[0]
            py = p[1]
            if px == x or py == y:
                continue

            if abs(px - x) != abs(py - y):
                continue

                
            count += self.pointCount[(x, py)] * self.pointCount[(px, y)]
                 
                
                # idk what to do
                # how do I check whether px exist as first and py as second in 
        return count
            

        
