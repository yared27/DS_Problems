a,b = map(int,input().split())
seq=[b]

while b>a:
    if b%2==0:
        b//=2
    elif b%10==1:
        b=(b-1)//10
    else:
        break
    seq.append(b)
if b==a:
    print("YES")
    print(len(seq))
    print(*reversed(seq))
else:
    print("NO")














































































































# from collections import Counter

# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     s = list(map(int, input().split()))
#     freq = Counter(s)
#     score = 0

#     for x in list(freq.keys()):
#         y = k - x
#         if x == y:
#             # Pair (x, x) can be made floor(freq[x] / 2) times
#             score += freq[x] // 2
#             freq[x] = 0
#         elif y in freq:
#             pairs = min(freq[x], freq[y])
#             score += pairs
#             freq[x] -= pairs
#             freq[y] -= pairs

#     print(score)
