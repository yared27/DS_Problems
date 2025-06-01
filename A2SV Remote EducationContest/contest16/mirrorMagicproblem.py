t = int(input())

charactersPair = {'p':'q','q':'p','w':'w'}

for _ in range(t):
    a = input()
    mirroredVersion = ''
    for i in reversed(a):
        mirroredVersion+=charactersPair[i]

    print(mirroredVersion)