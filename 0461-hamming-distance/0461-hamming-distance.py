class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x or y:
            if (x^y) & 1:
                ans+=1
            y >>= 1
            x >>= 1
        return ans 
                        