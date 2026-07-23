class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

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
            elif rank[pv] > rank[pu]:
                parent[pu] = pv
            else:
                parent[pv] = pu
                rank[pu] += 1

            return True

        for u, v in edges:
            if not union(u, v):
                return False

        return True