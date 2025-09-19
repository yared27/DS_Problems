class Solution:
    def primePalindrome(self, n: int) -> int:
        if 8 <= n <= 11:
            return 11

        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(math.isqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True

        for length in range(1, 6):  
            for half in range(10**(length-1), 10**length):
                s = str(half)
                palin = int(s + s[-2::-1])  
                if palin >= n and is_prime(palin):
                    return palin
