class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        numOfIslands=0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            stack = [(r,c)]
            grid[r][c] = "0"

            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if(nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc]=="0"):
                        continue
                    stack.append((nr, nc))
                    grid[nr][nc]="0"
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    numOfIslands+=1
        return numOfIslands