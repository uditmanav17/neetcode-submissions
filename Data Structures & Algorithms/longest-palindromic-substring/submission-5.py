class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)

        def check_palin(l, r):
            while l >= 0 and r < N and s[l] == s[r]:
                l -= 1
                r += 1
            return [l + 1, r]

        
        ans = [0, 0]
        for idx in range(N):
            odd_palin = check_palin(idx, idx)
            even_palin = check_palin(idx, idx + 1)
            ans = max(ans, odd_palin, even_palin, key=lambda x: x[1] - x[0])
        
        return s[ans[0]: ans[1]]


        