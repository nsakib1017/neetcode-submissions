class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        ROWS, COLS = len(grid), len(grid[0])
        minTime = 0

        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append((r,c,0))
        
        while q:
            r,c,t = q.popleft()
            minTime = max(t, minTime)
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==1):
                    grid[nr][nc] = 2
                    q.append((nr, nc, t+1))
                    fresh-=1
        return minTime if not fresh else -1
        
