from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        l1, l2 = len(text1), len(text2)

        @cache
        def helper(idx1, idx2):
            if idx1 >= l1 or idx2 >= l2:
                return 0

            ans = 0
            c1, c2 = text1[idx1], text2[idx2]
            if c1 == c2:
                ans = 1 + helper(idx1 + 1, idx2 + 1)
            else:
                ans = max(
                    helper(idx1 + 1, idx2),
                    helper(idx1, idx2 + 1)
                )
            return ans
        
        ans = helper(0, 0)
        return ans


        