class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.nthFibonacci(n-2) + self.nthFibonacci(n-1)
        
