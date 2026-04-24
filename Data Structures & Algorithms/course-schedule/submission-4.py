class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = defaultdict(list)
        for course, pre in prerequisites:
            preReq[course].append(pre)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if preReq[course] == []:
                return True
            
            visiting.add(course)
            for pre in preReq[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            preReq[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True            