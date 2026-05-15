class Solution:
    def factorial(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        for i in range(n):
            return n * self.factorial(n-1)