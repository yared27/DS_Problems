class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_occurrence(target):
            left = 0
            right = len(nums)-1
            ans=-1
            while left<=right:
                mid =(left+right)//2
                if nums[mid]>=target:
                    right=mid-1
                else:
                    left=mid+1
                if nums[mid]==target: 
                    ans=mid
            return ans

        def last_occurrence(target):
            right = len(nums)-1
            left = 0 
            ans=-1
            while left<=right:
                mid =(left+right)//2
                if nums[mid]<=target:
                    left=mid+1
                else:
                    right=mid-1
              
                if nums[mid]==target:
                    ans=mid
            return ans
        return [first_occurrence(target),last_occurrence(target)]
