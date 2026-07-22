class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses==0:
            return []
        indegree=[0]*numCourses
        D=defaultdict(list)
        for u,v in prerequisites:
            D[v].append(u)
            indegree[u]+=1
        res=[]
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
                res.append(i)
        while q:
            curr=q.popleft()
            for nei in D[curr]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
                    res.append(nei)
                    
        
        
        if len(res)==numCourses:
            return res
        return []