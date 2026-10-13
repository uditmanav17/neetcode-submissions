class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target, rem = divmod(total, k)
        if rem or max(nums) > target:
            return False
        
        ans = [0] * k
        N = len(nums)
        nums.sort(reverse=True)

        def helper(idx):
            if idx == N:
                return True
            ele = nums[idx]
            prev = -1
            for i in range(len(ans)):
                if ans[i] == prev or ans[i] + ele > target:
                    continue
                prev = ans[i]
                ans[i] += ele
                if helper(idx + 1):
                    return True
                ans[i] -= ele
            return False
            
        return helper(0)
                
