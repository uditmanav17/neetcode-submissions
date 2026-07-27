class Solution:
    def countSubstrings(self, s: str) -> int:

        def check_palin(l, r):
            count = 0
            while l >= 0 and r < N and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count

        
        ans = 0
        N = len(s)
        for idx in range(N):
            ans += check_palin(idx, idx)
            ans += check_palin(idx, idx + 1)
            
        return ans