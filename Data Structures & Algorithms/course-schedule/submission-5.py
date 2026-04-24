class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Count Indegree of each node
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        # 2. Add nodes with indegree = 0 to queue
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        finished = 0
        # 3. Traverse and decrease indegree. 
        #    if indegree == 0, add those to queue
        while q:
            node = q.popleft()
            finished += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return finished == numCourses
