class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            total = nums[l] + nums[r]
            if total == target:
                return [l + 1, r + 1]
            elif total > target:
                r -= 1
            elif total < target:
                l += 1

        