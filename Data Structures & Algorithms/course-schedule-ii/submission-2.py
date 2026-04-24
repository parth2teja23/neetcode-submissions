class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        indegree = [0] * numCourses
        adj = defaultdict(list)
        finished = 0
        # 1. Traverse and check indegree
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        # 2. add indegree = 0 to queue
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # 3. traverse and reduce indegree.
        #   if indegree is 0, add it to queue
        while q:
            node = q.popleft()
            res.append(node)
            finished += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return res if finished == numCourses else []