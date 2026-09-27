class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        ans = run_sum = 0
        
        for idx, ele in enumerate(nums):
            run_sum += ele
            diff = run_sum - k
            
            ans += seen.get(diff, 0)
            seen[run_sum] = seen.get(run_sum, 0) + 1

        return ans

        