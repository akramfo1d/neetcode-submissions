from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph and indegree
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Add all nodes with indegree 0
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        completed = 0

        while q:
            node = q.popleft()
            completed += 1

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return completed == numCourses