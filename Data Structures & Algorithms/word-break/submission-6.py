from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)

        @cache
        def helper(start_idx):
            if start_idx >= N:
                return True
            
            ans = False
            for word in wordDict:
                w_len = len(word)
                end_idx = start_idx + w_len
                sliced_word = s[start_idx: end_idx]
                if sliced_word == word:
                    ans |= helper(end_idx)
                    if ans: 
                        return ans
            return ans

        return helper(0)
