class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        for idx, ele in enumerate(nums):
            ans ^= idx ^ ele
        return ans
        