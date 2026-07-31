from functools import cache

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        @cache
        def helper(idx, cap):
            if cap <= 0 or idx >= len(weight):
                return 0
            
            wt = weight[idx]
            gain = profit[idx]

            take = 0
            if cap - wt >= 0:
                take = gain + helper(idx + 1, cap - wt)
    
            skip = helper(idx + 1, cap)

            return max(take, skip)

        ans = helper(0, capacity)
        return ans
