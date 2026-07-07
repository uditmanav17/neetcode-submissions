class Solution:
    def isPalindrome(self, s: str) -> bool:
        N = len(s)
        l, r = 0, N - 1

        while l < r:
            l_char = s[l].lower()
            r_char = s[r].lower()

            if not l_char.isalnum():
                l += 1
                continue

            if not r_char.isalnum():
                r -= 1
                continue
        
            if l_char == r_char:
                l += 1
                r -= 1
            else:
                return False
            
        return True