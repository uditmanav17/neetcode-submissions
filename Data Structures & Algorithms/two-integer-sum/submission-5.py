class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, ele in enumerate(nums):
            diff = target - ele
            if diff in seen:
                return [seen.get(diff), idx]
            seen[ele] = idx