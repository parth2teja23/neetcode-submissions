# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         adj = [[] for _ in range(n)]
#         visited = [False] * n

#         for edge in edges:
#             adj[edge[0]].append(edge[1])
#             adj[edge[1]].append(edge[0])

#         def dfs(node):
#             for nei in adj[node]:
#                 if not visited[node]:
#                     visited[nei] = True
#                     dfs(nei)
        
#         res = 0

#         for i in range(n):
#             if not visited[i]:
#                 visited[i] = True
#                 dfs(i)
#                 res += 1
#         return res


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res
        