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
        






































































# import sys
# from collections import Counter
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     freq = Counter(arr)

#     score = 0
#     visited = set()

#     for x in freq:
#         y = k - x
#         if y in freq and x not in visited and y not in visited:
#             if x == y:
#                 score += freq[x] // 2
#             else:
#                 score += min(freq[x], freq[y])
#             visited.add(x)
#             visited.add(y)

#     # Score cannot exceed n//2 (total pairs possible)
#     print(min(score, n // 2))
