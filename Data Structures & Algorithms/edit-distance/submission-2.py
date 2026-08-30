from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def helper(idx1, idx2):
            if idx1 == 0 or idx2 == 0:
                return idx1 or idx2
            c1 = word1[idx1 - 1]
            c2 = word2[idx2 - 1]
            if c1 == c2:
                return helper(idx1 - 1, idx2 - 1)
            if c1 != c2:
                return 1 + min(
                    helper(idx1 - 1, idx2 - 1),
                    helper(idx1 - 1, idx2),
                    helper(idx1, idx2 - 1),
                )
        
        l1, l2 = len(word1), len(word2)
        return helper(l1, l2)
