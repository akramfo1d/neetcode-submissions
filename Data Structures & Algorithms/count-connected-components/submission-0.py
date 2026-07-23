class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n
        components = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            nonlocal components
            pa, pb = find(a), find(b)

            if pa == pb:
                return

            if rank[pa] > rank[pb]:
                parent[pb] = pa
            elif rank[pa] < rank[pb]:
                parent[pa] = pb
            else:
                parent[pb] = pa
                rank[pa] += 1

            components -= 1

        for u, v in edges:
            union(u, v)

        return components