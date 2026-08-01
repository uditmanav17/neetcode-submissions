from functools import cache

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        N = len(profit)

        @cache
        def helper(idx, cap):
            if idx >= N or cap < 0:
                return 0
            
            wt = weight[idx]
            gain = profit[idx]

            take1 = take2 = 0
            if cap - wt >= 0:
                take1 = gain + helper(idx, cap - wt)
                take2 = gain + helper(idx + 1, cap - wt)
            skip = helper(idx + 1, cap)

            return max(take1, take2, skip)
        
        return helper(0, capacity)
