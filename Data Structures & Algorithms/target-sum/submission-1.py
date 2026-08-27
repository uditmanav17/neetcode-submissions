from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def helper(idx, remain):
            if idx >= len(nums):
                if remain == 0:
                    return 1
                return 0
            ans = 0
            ele = nums[idx]
            ans += helper(idx + 1, remain - ele)
            ans += helper(idx + 1, remain + ele)
            return ans

        return helper(0, target)
        
        