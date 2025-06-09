from collections import Counter
t = int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=list(map(int, input().split()))
    freq= Counter(s)
    score=0
    for x in list(freq.keys()):
        y=k-x
        if x==y:
            score+=freq[x]//2
            freq[x]=0
        elif y in freq:
            pairs=min(freq[x],freq[y])
            score += pairs
            freq[x] -= pairs
            freq[y] -= pairs
    print(score)
        






































































