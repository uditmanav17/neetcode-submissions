from functools import cache
from math import inf

class Solution:
    def numSquares(self, n: int) -> int:
        
        @cache
        def helper(num):
            if num in (1, 0):
                return num
            ans = inf
            for i in range(100, 0, -1):
                if num >= i * i:
                    ans = min(ans, 1 + helper(num - i * i))
            return ans
        
        return helper(n)
