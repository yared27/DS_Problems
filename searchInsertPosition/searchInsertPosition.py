arr = []

n= int(input("Enter the number of element"))

print("Enter the element")
for i in range(n):
    arr.append(int(input()))
target = int(input('Enter the the target number'))
def searchInsert(nums, target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (r + l) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return l

print(searchInsert(arr,target))