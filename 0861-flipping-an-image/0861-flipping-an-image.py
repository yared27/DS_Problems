class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i,row in enumerate(image):
            row.reverse()
            for j in range(len(row)):
                    image[i][j]=1-image[i][j]
               
        return image
                



