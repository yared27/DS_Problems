class Solution:
    def fib(self, n: int) -> int:
        preprev = 0 
        prev = 1
        for i in range(2,n+1):
            temp  = prev
            prev = prev + preprev
            preprev = temp
        return prev if n != 0 else 0
       