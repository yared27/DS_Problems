class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index = 0
        maxOne =0
        for i,row in enumerate(mat):
            noOne =row.count(1)
            if noOne>maxOne:
                maxOne = noOne
                index=i
        return [index,maxOne]

