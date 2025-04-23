
nums = list(map(int,input().split()))
target = int(input("Enter the target"))
def minSubArrayLen( target: int, nums) -> int:
    minL = 10 ** 9
    left = 0
    result = 0
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        while sum >= target:
            minL = min(minL, (i - left + 1))
            result = minL
            sum -= nums[left]
            left += 1

    return result

minSubArrayLen(target,nums)
