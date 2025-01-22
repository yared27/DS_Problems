arr=[1,100,1,1,1,100,1,1,100,1]
arr.append(0)
for i in range(len(arr)-3,-1,-1):
    arr[i]+=min(arr[i+1],arr[i+2])
print(arr)
print(min(arr[0],arr[1]))