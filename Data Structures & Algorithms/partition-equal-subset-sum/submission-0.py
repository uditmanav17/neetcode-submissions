from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        @cache
        def helper(idx, curr_sum):
            if idx >= len(nums):
                return curr_sum == target
            
            ele = nums[idx]
            
            pick = helper(idx + 1, curr_sum + ele)
            skip = helper(idx + 1, curr_sum)
            
            return pick or skip
        
        return helper(0, 0)

        