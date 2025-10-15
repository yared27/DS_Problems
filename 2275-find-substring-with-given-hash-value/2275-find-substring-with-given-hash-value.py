class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        h = 0
        ans = 0

        p = pow(power, k, modulo)

        for i in range(n - 1, -1, -1):
            val = ord(s[i]) - ord('a') + 1
            h = (h * power + val) % modulo

            if i + k <= n - 1:
                out_val = ord(s[i + k]) - ord('a') + 1
                h = (h - out_val * p) % modulo 

            if i + k - 1 < n and h == hashValue:
                ans = i  
        return s[ans:ans + k]
