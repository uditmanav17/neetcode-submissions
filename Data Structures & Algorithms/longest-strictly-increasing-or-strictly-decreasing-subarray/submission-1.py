class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = inc = dec = 1

        for idx in range(1, len(nums)):
            if nums[idx - 1] < nums[idx]:
                inc += 1
                dec = 1
            elif nums[idx - 1] > nums[idx]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            print(idx, inc, dec)
            ans = max(ans, inc, dec)
        
        return ans

        