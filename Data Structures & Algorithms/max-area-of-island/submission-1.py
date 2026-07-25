class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        MaxArea=0

        visit=set()
        rows,cols=len(grid),len(grid[0])
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visit.add((r,c))
            Area=1
            while q:
                r,c=q.popleft()
                directions=[(0,1),(1,0),(0,-1),(-1,0)]
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if(nr in range(rows) and nc in range(cols) and grid[nr][nc]==1 and (nr,nc) not in visit):
                        Area+=1
                        visit.add((nr,nc))
                        q.append((nr,nc))
            return Area

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    Area=bfs(r,c)
                    MaxArea=max(MaxArea,Area)
                
        return MaxArea