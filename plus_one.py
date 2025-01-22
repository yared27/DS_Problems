n=int(input("Enter the number of element"))
arr=[]
print("Enter list element")
for i in range(n):
    arr.append(int(input()))
def plus_one(arr):
    arr=int(''.join(map(str,arr)))
    arr+=1
    arr=str(arr)
    return list(map(int,arr))
print(plus_one(arr))