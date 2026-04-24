class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for time in times:
            u = time[0]
            v = time[1]
            w = time[2]

            graph[u].append((v, w))

        pq = [(0,k)] # [(time, node)]
        visited = {}

        while pq:
            time, node = heapq.heappop(pq)
            if node in visited:
                continue
            
            visited[node] =time
            
            for nei, weight in graph[node]:
                if nei not in visited:
                    heapq.heappush(pq, (time + weight, nei))
        
        if len(visited) == n:
            return max(visited.values())
        return -1
