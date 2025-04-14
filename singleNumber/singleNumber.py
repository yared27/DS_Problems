arr = []

n= int(input("Enter the number of element"))

print("Enter the element")
for i in range(n):
    arr.append(int(input()))


def singleNumber(self, nums: List[int]) -> int:
    result = 0
    for i in nums:
        result ^= i

    return result
singleNumber(arr)