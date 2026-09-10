class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def digit_sq(num):
            total = 0
            while num:
                num, r = divmod(num, 10)
                total += r ** 2
            return total

        while n != 1 and n not in seen:
            seen.add(n)
            n = digit_sq(n)
        return n == 1
            
