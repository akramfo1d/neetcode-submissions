class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, cols = len(board), len(board[0])

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != "O"
            ):
                return

            board[r][c] = "T"

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Top and bottom rows
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Left and right columns
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        # Flip surrounded O's and restore safe O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"