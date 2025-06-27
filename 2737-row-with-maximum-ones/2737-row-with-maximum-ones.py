class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index = -1
        noOne =0
        indexVal ={}
        for i in range(len(mat)):
            currentNumberOfOne = 0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    currentNumberOfOne+=1
            if currentNumberOfOne in indexVal:
                indexVal[currentNumberOfOne] = min(indexVal[currentNumberOfOne],i)
            else:
                indexVal[currentNumberOfOne]=i
            noOne=max(noOne,currentNumberOfOne)
        return [indexVal[noOne],noOne]


