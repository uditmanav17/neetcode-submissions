class Solution:

    def rob_helper(self, nums: List[int]) -> int:
        N = len(nums)
        dp0, dp1 = nums[0], max(nums[:2])
        
        for idx in range(2, N):
            dp0, dp1 = dp1, max(dp1, dp0 + nums[idx])
        
        return max(dp0, dp1)

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        return max(
            self.rob_helper(nums[1:]),
            self.rob_helper(nums[:-1]),
        )
        