class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        areaMax = 0
        while i<j:
            areaMax = max(areaMax,((j-i)*min(height[i], height[j])))
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
            
        return areaMax



