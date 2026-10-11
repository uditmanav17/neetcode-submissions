class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N =len(nums)

        def helper(idx, curr, ans):
            if idx >= N:
                ans.append(curr[:])
                return 
            ele = nums[idx]
            helper(idx + 1, curr + [ele], ans)
            helper(idx + 1, curr, ans)

        ans = []
        helper(0, [], ans)
        return ans