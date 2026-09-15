class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(sources):
            q = deque((r, c, 0) for r, c in sources)
            visit = set(sources)
            while q:
                r, c, d = q.popleft()
                grid[r][c] = d
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS
                            and (nr, nc) not in visit
                            and grid[nr][nc] != -1):
                        visit.add((nr, nc))
                        q.append((nr, nc, d + 1))

        chests = [(r, c)
                  for r in range(ROWS) for c in range(COLS)
                  if grid[r][c] == 0]
        bfs(chests)