t = int(input())

charactersPair = {'p':'q','q':'p','w':'w'}

for _ in range(t):
    a = input()
    mirroredVersion = ''
    for i in reversed(a):
        mirroredVersion+=charactersPair[i]

    print(mirroredVersion)

#  goal
#  For each input string, produce its mirrored version
#  Reversing the string (mirror flips direction)
#    p to q
#    q to p
#    w-w(no change)
#      qwq
#      pwp
# aproach:
#         1.revering the string a
#         2.Use a dictionary (charactersPair)
