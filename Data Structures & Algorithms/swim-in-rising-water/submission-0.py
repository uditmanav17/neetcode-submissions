from heapq import heappop, heappush

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])
        seen = set([(0, 0)])
        heap = [(grid[0][0], 0, 0)]
        
        time = 0
        while heap:
            while heap[0][0] <= time:
                val, r, c = heappop(heap)
                if r == ROWS - 1 and c == COLS - 1:
                    return time
                for dx, dy in dirs:
                    nr, nc = r + dx, c + dy
                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and (nr, nc) not in seen
                    ):
                        heappush(heap, (grid[nr][nc], nr, nc))
                        seen.add((nr, nc))
            time += 1
        
                
                
