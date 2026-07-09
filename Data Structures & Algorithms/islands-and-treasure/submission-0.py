from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()

        # Add all gates to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        def bfs():
            directions = [(1,0), (0,1), (-1,0), (0,-1)]

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visit
                        and grid[nr][nc] != -1
                    ):
                        grid[nr][nc] = grid[r][c] + 1
                        visit.add((nr, nc))
                        q.append((nr, nc))

        bfs()