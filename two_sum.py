n=int(input("Enter the number of element"))
target=int(input("Enter the targets"))
arr=[]
print("Enter the Elements")
for i in range(n):
    arr.append(int(input()))
def is_there(arr,t):
    seen={}
    for i,value in enumerate(arr):
        a=t-value
        if a in seen:
               return seen[a],i
        else :
            seen[value]=i
print(is_there(arr,target))