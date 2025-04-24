class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        output = []

        for i in range(n):
            total = 0
            if k > 0:
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
            elif k < 0:
                for j in range(1, -k + 1):
                    total += code[(i - j) % n]
            output.append(total)

        return output