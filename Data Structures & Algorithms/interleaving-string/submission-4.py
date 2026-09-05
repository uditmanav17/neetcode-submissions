from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        
        @cache
        def helper(i1, i2):
            i3 = i1 + i2

            if i1 >= l1:
                return s2[i2:] == s3[i3:]
            if i2 >= l2:
                return s1[i1:] == s3[i3:]
            
            ans = False
            c1, c2, c3 = s1[i1], s2[i2], s3[i3]
            if c1 == c3 == c2:
                ans |= helper(i1 + 1, i2) or helper(i1, i2 + 1)
            elif c1 == c3:
                ans |= helper(i1 + 1, i2)
            elif c2 == c3:
                ans |= helper(i1, i2 + 1)
            return ans
        
        return helper(0, 0)
