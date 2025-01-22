import string
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for char in columnTitle:
            value = ord(char) - ord("A") + 1
            ans = ans * 26 + value
        return ans
sol=Solution()
title=input("Enter the title ").upper()
print(sol.titleToNumber(title))