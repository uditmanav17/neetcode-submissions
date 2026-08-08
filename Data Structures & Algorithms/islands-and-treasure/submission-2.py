from itertools import product
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for r, c in product(range(ROWS), range(COLS)):
            if grid[r][c] == 0:
                q.append((r, c, 0))

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            cr, cc, step = q.popleft()
            for dx, dy in dirs:
                nr, nc = cr + dx, cc + dy
                if (
                    0 <= nr < ROWS 
                    and 0 <= nc < COLS
                    and (nr, nc) != -1
                    and grid[nr][nc] == 2147483647
                ):
                    grid[nr][nc] = step + 1
                    q.append((nr, nc, step + 1))
        




        