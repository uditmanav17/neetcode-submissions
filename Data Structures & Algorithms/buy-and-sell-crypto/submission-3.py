from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = inf
        for p in prices:
            buy = min(buy, p)
            profit = p - buy
            ans = max(ans, profit)
        return ans
        