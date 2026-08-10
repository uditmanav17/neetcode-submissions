from math import inf

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -inf
        run_sum = 0

        for ele in nums:
            run_sum = max(ele, run_sum + ele)
            max_sum = max(max_sum, run_sum)

        return max_sum
        