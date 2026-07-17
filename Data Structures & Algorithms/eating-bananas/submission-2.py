from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            mid = l + (r - l) // 2
            time_taken = sum(ceil(pile / mid) for pile in piles)
            # print(mid, time_taken)
            if time_taken > h:
                l = mid + 1
            else:
                r = mid - 1
        return l

        