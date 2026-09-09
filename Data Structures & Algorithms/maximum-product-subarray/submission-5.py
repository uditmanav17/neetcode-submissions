from math import inf

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = suffix = 1
        ans = -inf
        
        for idx in range(N):
            prefix = (prefix or 1) * nums[idx]
            suffix = (suffix or 1) * nums[N - idx - 1]
            ans = max(ans, prefix, suffix)
        
        return ans






        