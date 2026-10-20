
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        visit = set()
        rows, cols = len(grid), len(grid[0])
        maxarea = 0

        def bfs(r, c):
            visit.add((r, c))
            queue = deque([(r, c)])
            area = 1

            directions = [
                (0, 1), (1, 0),
                (-1, 0), (0, -1)
            ]

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        (nr, nc) not in visit and
                        grid[nr][nc] == 1
                    ):
                        area += 1
                        queue.append((nr, nc))
                        visit.add((nr, nc))

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxarea = max(bfs(r, c), maxarea)

        return maxarea
