
arr = []

n= int(input("Enter the number of element"))

print("Enter the element")
for i in range(n):
    arr.append(int(input()))


def missingNumber(nums )-> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    print((expected_sum))
    actuall_sum = sum(nums)
    print(actuall_sum)

    return expected_sum - actuall_sum


print(missingNumber(arr))