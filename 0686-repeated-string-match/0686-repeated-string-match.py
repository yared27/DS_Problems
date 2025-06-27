class Solution(object):
    def repeatedStringMatch(self, a, b):
        q = (len(b) - 1) // len(a) + 1
        for i in range(2):
            if b in a * (q+i): return q+i
        return -1