class Solution:

    def get_fresh_rotten_count(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0

        for r, c in product(range(ROWS), range(COLS)):
            if grid[r][c] == 2:
                rotten.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
        return rotten, fresh


    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rotten, fresh = self.get_fresh_rotten_count(grid)
        if not rotten and fresh:
            return -1
        if fresh == 0:
            return 0
        
        time = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while rotten:
            N = len(rotten)
            for _ in range(N):
                cr, cc = rotten.popleft()
                for dx, dy in dirs:
                    nr, nc = cr + dx, cc + dy
                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        # and (nr, nc) == 1
                        and grid[nr][nc] == 1
                    ):
                        rotten.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            time += 1
        

        return time - 1 if not fresh else -1


        