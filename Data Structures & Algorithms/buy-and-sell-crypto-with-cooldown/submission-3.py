from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @cache
        def helper(s_idx, buy=True):
            if s_idx >= len(prices):
                return 0
            buy_price = sell_price = 0
            do_nothing = helper(s_idx + 1, buy)

            if buy:
                buy_price = helper(s_idx + 1, False) - prices[s_idx]
            else:
                # cool down of 1 day
                sell_price = helper(s_idx + 2, True) + prices[s_idx]

            return max(buy_price, sell_price, do_nothing)

        return helper(0)
        