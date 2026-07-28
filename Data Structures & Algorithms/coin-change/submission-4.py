from math import inf
from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        @cache
        def helper(idx, remain):
            if idx > len(coins) or remain < 0:
                return inf
            if remain == 0:
                return 0
            ans = inf
            for i in range(idx, len(coins)):
                coin = coins[i]
                if remain - coin >= 0:
                    temp_ans = 1 + helper(idx, remain - coin)
                    ans = min(ans, temp_ans)
            return ans
        
        ans = helper(0, amount)
        return ans if ans != inf else -1


            
