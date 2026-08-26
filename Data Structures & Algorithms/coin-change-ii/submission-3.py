from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        @cache
        def helper(remain, coin_idx):
            if remain == 0:
                return 1
            if remain < 0 or coin_idx >= len(coins):
                return 0
            ans = 0
            curr_coin = coins[coin_idx]
            if remain >= curr_coin:
                ans += helper(remain - curr_coin, coin_idx)
            ans += helper(remain, coin_idx + 1)
            return ans

        return helper(amount, 0)
    