class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        def reverse_num(num):
            rev = 0
            while num:
                num, last = divmod(num, 10)
                rev = rev * 10 + last
            return rev

        return reverse_num(x) == x
