class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        def countOnes(num):
            noOne = 0
            while num:
                if num & 1:
                    noOne += 1
                num >>= 1
            return noOne
        for i in range(n+1):
            output.append(countOnes(i))
        
        return output
                  
        