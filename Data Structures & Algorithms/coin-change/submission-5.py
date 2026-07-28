from math import inf
from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        @cache
        def helper(idx, remain):
            if remain == 0:
                return 0
            if idx == len(coins) or remain < 0:
                return inf
            # skip current coin
            skip = helper(idx + 1, remain)
            # use current coin
            use = 1 + helper(idx, remain - coins[idx])
            return min(skip, use)
        
        ans = helper(0, amount)
        return ans if ans != inf else -1


            
