from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num = factorial(m + n - 2)
        deno = factorial(m - 1) * factorial(n - 1)
        return num // deno
        