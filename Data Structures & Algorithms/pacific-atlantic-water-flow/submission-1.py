class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        pac,atl=set(),set()

        def dfs(r,c,h, visit):
            stack = [(r,c,h)]
            visit.add((r,c))

            while stack:
                row, col, prevH = stack.pop()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (0<=nr<ROWS and 0<=nc<COLS and heights[nr][nc]>=prevH and (nr, nc) not in visit):
                        stack.append((nr,nc,heights[nr][nc]))
                        visit.add((nr,nc))
        
        for r in range(ROWS):
            dfs(r,0,heights[r][0],pac)
            dfs(r,COLS-1,heights[r][COLS-1],atl)
        for c in range(COLS):
            dfs(0,c, heights[0][c], pac)
            dfs(ROWS-1,c, heights[ROWS-1][c], atl)

        results = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    results.append([r,c])
        return results
