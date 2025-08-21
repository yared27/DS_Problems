class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        def countOnes(num):
            ct = 0
            print(num)

            while num:
                if num&1==1:
                    ct+=1
                num >>= 1
                print(num)
            return ct
        
        for i in range(n+1):
            num_bits = countOnes(i)
            output.append(num_bits)
        return output

