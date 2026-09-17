class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        pac,atl = set(),set()

        def dfs(r, c, visit, h):
            stack = [(r,c, h)]
            visit.add((r,c))
            
            while stack:
                row, col, prevHeight = stack.pop()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visit and heights[nr][nc] >= prevHeight):
                        visit.add((nr,nc))
                        stack.append((nr,nc,heights[nr][nc]))
            
        for c in range(COLS):
                dfs(0, c, pac, heights[0][c])
                dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
                dfs(r, 0, pac, heights[r][0])
                dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                        res.append([r, c])
        return res