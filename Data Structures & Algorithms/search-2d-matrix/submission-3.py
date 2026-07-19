class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            mid = l + (r - l) // 2
            cr, cc = mid // COLS, mid % COLS
            ele = matrix[cr][cc]
            if ele == target:
                return True
            if ele > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

        