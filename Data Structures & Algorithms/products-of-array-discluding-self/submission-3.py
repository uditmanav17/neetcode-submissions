class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        prefix = suffix = 1
        ans = [1] * N 

        for idx, ele in enumerate(nums):
            ans[idx] *= prefix
            prefix *= ele

            l_idx = N - idx - 1
            ans[l_idx] *= suffix
            suffix *= nums[l_idx]
        
        return ans

        