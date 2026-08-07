from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        
        N = len(s)

        @cache
        def helper(idx):
            if idx >= N:
                return 1
            
            ans = 0

            c1 = s[idx]
            if 1 <= int(c1) <= 9:
                ans += helper(idx + 1)
            
            c2 = s[idx: idx + 2]
            if 10 <= int(c2) <= 26:
                ans += helper(idx + 2)
            
            return ans
        
        return helper(0)

