from functools import cache

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        N = len(profit)

        @cache
        def helper(idx, cap):
            if idx >= N or cap <= 0:
                return 0
            
            wt = weight[idx]
            gain = profit[idx]

            take = 0
            if cap - wt >= 0:
                take = gain + helper(idx, cap - wt)
            skip = helper(idx + 1, cap)

            return max(take, skip)
        
        return helper(0, capacity)
