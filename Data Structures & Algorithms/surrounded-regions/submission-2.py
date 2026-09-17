class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c):
            stack = [(r,c)]
            board[r][c] = "T"
            
            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    nr, nc = row+dr, col + dc
                    if(0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc]=="O"):
                        stack.append((nr,nc))
                        board[nr][nc] = "T"
        
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS-1] == "O":
                dfs(r,COLS-1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
