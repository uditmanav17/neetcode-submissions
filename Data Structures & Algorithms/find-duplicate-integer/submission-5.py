class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = 0
        for ele in nums:
            pos = 1 << ele
            if ans & pos != 0:
                return ele
            ans |= pos
