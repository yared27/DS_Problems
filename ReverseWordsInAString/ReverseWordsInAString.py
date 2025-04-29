class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split()
        i = 0
        j = len(slist) - 1

        while i <= j:
            slist[i], slist[j] = slist[j], slist[i]
            i += 1
            j -= 1
        return " ".join(slist)
