class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newArr = []
        i = 0
        j = n
        while j<(2*n) and i<n:
                newArr.append(nums[i])
                i += 1
                newArr.append(nums[j])
                j += 1
        return newArr

