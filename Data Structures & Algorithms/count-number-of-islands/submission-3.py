from collections import deque
from itertools import product

class Solution:

    def bfs(self, r, c, grid, visited):
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([(r, c)])
        visited.add((r, c))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            cr, cc = q.popleft()
            for dx, dy in dirs:
                nr, nc = cr + dx, cc + dy
                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and (nr, nc) not in visited
                    and grid[nr][nc] == "1"
                ):
                    q.append((nr, nc))
                    visited.add((nr, nc))
        
            
        



    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        for r, c in product(range(ROWS), range(COLS)):
            if grid[r][c] == "1" and (r, c) not in visited:
                self.bfs(r, c, grid, visited)
                islands += 1
        return islands

        