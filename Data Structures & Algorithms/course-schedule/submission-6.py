# Topological Sort (Kahn's Algorithm)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1.Count courses with 0 prerequisites
        indegree = [0] * numCourses
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
            
        # 2. put nodes with 0 indegree to queue
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # 3. process the node and reduce indegree.
        #   Add nodes with 0 indegree back to queue
        finished = 0
        while q:
            node = q.popleft()
            finished += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return finished == numCourses