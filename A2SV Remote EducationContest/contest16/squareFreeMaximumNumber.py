import math
n = int(input())
numbers = list(map(int,input().split()))
nonePerfectSquare = []
for i in numbers:
    if i<0:
        nonePerfectSquare.append(i)
    elif not math.sqrt(i).is_integer():
        nonePerfectSquare.append(i)
print(max(nonePerfectSquare))