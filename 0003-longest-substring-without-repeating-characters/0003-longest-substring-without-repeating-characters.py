class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterOccurrence = {}
        i = 0
        j = 0
        maxLen = 0
        while j < len(s):
            if s[j] not in s[i:j]:
                j += 1
                maxLen = max(maxLen,j-i)
            else:
                i += 1
        return maxLen

            

