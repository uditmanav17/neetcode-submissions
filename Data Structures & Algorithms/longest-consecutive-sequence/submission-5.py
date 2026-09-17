class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seen = set()
        ans = 0

        for ele in nums:
            if ele in seen:
                continue

            l = ele - 1
            while l in nums:
                seen.add(l)
                l -= 1

            r = ele + 1
            while r in nums:
                seen.add(r)
                r += 1
            
            ans = max(ans, r - l - 1)
        
        return ans
