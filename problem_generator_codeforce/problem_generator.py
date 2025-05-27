import collections
a = input("Enter the problems")
n = int(input("Enter the number of element"))
round = int(input("Enter the number of round"))

def findRemainingProblems(a,round):
    freq = collections.Counter(a)
    needed =0
    problemDifficulty = "ABCDEFG"
    for i in problemDifficulty:
        have = freq.get(i,0)
        if have<round:
            needed+= round-have
    return needed
print(findRemainingProblems(a,round))


