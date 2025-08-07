class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1,numRows):
            prev = ans[i-1]
            currentRow = [1]

            for j in range(1, i):
                sum_val = prev[j-1] + prev[j]
                currentRow.append(sum_val)
            
            currentRow.append(1)

            ans.append(currentRow)
        return ans
