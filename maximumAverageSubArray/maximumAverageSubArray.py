
num = list(map(int,input().split(",")))
k = int(input("Enter k"))
def findMaxAverage(nums, k: int) -> float:
    summ = sum(nums[:k])
    ans = summ
    for i in range(k, len(nums)):
        summ += nums[i] - nums[i - k]
        ans = max(ans, summ)
    return ans / k


print(findMaxAverage(num,k))