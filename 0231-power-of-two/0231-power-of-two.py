class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n>=1:
            if n == 1:
                return True
            n/=2
        return False