class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. find all nodes with 0 indegree
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] +=1

        # 2. add nodes with indegree = 0 to queue
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        # 3. process nodes and reduce indegree.
        #   Add nodes with 0 indegree back to queue
        res = []
        finished = 0
        while q:
            node = q.popleft()
            res.append(node)
            finished += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if finished == numCourses else []
