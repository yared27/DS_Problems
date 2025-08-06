class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        currentRow = []

        currentRow.append(1)

        for i in range(1,rowIndex + 1):
            newRow = []

            newRow.append(1)

            for j in range(1, i):
                sum_val = currentRow[j-1] + currentRow[j]
                newRow.append(sum_val)
            
            newRow.append(1)

            currentRow = newRow
        return currentRow

        