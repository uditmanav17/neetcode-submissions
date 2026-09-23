from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for ele in nums:
            if not ans or ans[-1] < ele:
                ans.append(ele)
            else:
                idx = bisect_left(ans, ele)
                ans[idx] = ele
        return len(ans)

        