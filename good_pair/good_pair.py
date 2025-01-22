import collections

num=int(input("Enter the number element"))
lis=[]
print("Enter elements")
for i in range(num):
    lis.append(input())
def good_pair(lis):
    count=collections.Counter(lis)
    ans=0
    for i  in count.values():
        if i>1:
         ans+=sum(range(i))
    return ans
print(good_pair(lis))