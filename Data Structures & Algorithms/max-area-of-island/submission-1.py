from collections import deque
from itertools import product

class Solution:
    def get_area(self, row, col, grid, visited):
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([(row, col)])
        visited.add((row, col))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        area = 1
        while q:
            r, c = q.popleft()
            for dx, dy in dirs:
                nr, nc = r + dx, c + dy
                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and grid[nr][nc] != 0
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    q.append((nr, nc))
                    area += 1
        return area


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        for r, c in product(range(ROWS), range(COLS)):
            if grid[r][c] == 1 and (r, c) not in visited:
                max_area = max(max_area, self.get_area(r, c, grid, visited))
        return max_area


        