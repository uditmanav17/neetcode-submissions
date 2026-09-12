from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        N = len(s)

        @cache
        def helper(start_idx):
            if start_idx >= N:
                return True
            for idx in range(start_idx, N):
                curr_word = s[start_idx:idx + 1]
                if curr_word in words and helper(idx + 1):
                    return True
            return False

        return helper(0)

        