class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [0,-1], [1,0],[-1,0]]
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            dfsStack = [(r,c)]
            grid[r][c] = 0
            res = 1
            while dfsStack:
                row, col = dfsStack.pop()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if(nr < 0 or nc < 0 or nr>=ROWS or nc >=COLS or grid[nr][nc]==0):
                        continue
                    dfsStack.append((nr, nc))
                    res+=1
                    grid[nr][nc] = 0
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    maxArea = max(area, maxArea)
        return maxArea

