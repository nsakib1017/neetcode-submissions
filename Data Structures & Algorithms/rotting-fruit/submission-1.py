class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0),(0,1), (0,-1)]
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        q=deque()
        fresh = 0
        minTime = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append((r,c,0))
                    visited.add((r,c))
        
        while q:
            r, c, t = q.popleft()
            minTime = max(minTime, t)
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (0<=nr<ROWS and 0<=nc<COLS 
                    and (nr, nc) not in visited 
                    and grid[nr][nc]==1):
                        visited.add((nr,nc))
                        fresh-=1
                        q.append((nr,nc, t+1))
        return minTime if not fresh else -1
