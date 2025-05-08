class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        j = len(s1)
        for i in range(len(s2)-j+1):
            if sorted(s2[i:i+j]) == sorted(s1):
                return True
        return False