class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        D=defaultdict(list)
        for u,v in prerequisites:
            D[u].append(v)

        unvisited=0
        visited=2
        visiting=1

        check=[unvisited]*(numCourses)


        def dfs(node):
            if check[node]==visiting:
                return False
            if check[node]==visited:
                return True

            check[node]=visiting

            for nei in D[node]:
                if not dfs(nei):
                    return False

            check[node]=visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
            
