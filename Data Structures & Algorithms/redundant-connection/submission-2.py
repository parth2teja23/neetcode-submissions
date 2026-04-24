class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(u, v):
            pu = find(u)
            pv = find(v)

            if pu == pv:
                return False
            if rank[pv] > rank[pu]:
                pu, pv = pv, pu
            parent[pv] = pu
            rank[pu] += rank[pv]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

            
            
            
        