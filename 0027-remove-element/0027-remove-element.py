class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j =0
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                print(nums[i])
                nums[j]=nums[i]
                j+=1
                k+=1     
        return k

        