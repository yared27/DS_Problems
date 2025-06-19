class Solution:
    def reverseWords(self, s: str) -> str:
        spaceSeparated=s.split()
        left=0
        right=len(spaceSeparated)-1
        while left<right:
            spaceSeparated[right], spaceSeparated[left]=spaceSeparated[left],spaceSeparated[right]
            left+=1
            right-=1
        return " ".join(spaceSeparated)