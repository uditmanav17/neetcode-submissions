class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1 or n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return self.myPow(1/x, -n)
        
        if n % 2 == 0:
            temp_ans = self.myPow(x, n // 2)
            return temp_ans * temp_ans
        else:
            return x * self.myPow(x, n - 1)

        