class Solution:
    def findRedundantConnection(self, edges: List[List[int]]):
        n = len(edges) + 1
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            pu, pv = find(u), find(v)

            if pu == pv:
                return False

            if rank[pu] > rank[pv]:
                parent[pv] = pu
            elif rank[pu] < rank[pv]:
                parent[pu] = pv
            else:
                parent[pu] = pv
                rank[pv] += 1

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]