arr = []

n= int(input("Enter the number of element"))

print("Enter the element")
for i in range(n):
    arr.append(int(input()))

def summaryRanges(self, nums: List[int]) -> List[str]:
    start = ''
    output = []
    for i in range(len(nums)):
        if start == "":
            start = nums[i]
        elif (nums[i - 1] + 1 != nums[i]):
            if start == nums[i - 1]:
                output.append(str(start))
            else:
                start = str(start)
                start += "->" + str(nums[i - 1])
                output.append(start)
            start = nums[i]

    if start != '':
        if start == nums[-1]:
            output.append(str(start))
        else:
            output.append(f"{start}->{nums[-1]}")
    return output

print(summaryRanges(arr))
