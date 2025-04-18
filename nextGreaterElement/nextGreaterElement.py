arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

def nextGreaterElement(nums1, nums2):
        output=[-1]*len(nums1)
        dic_num1={n:i for i,n in enumerate(nums1)}
        stack=[]
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr>stack[-1]:
                val=stack.pop()
                index= dic_num1[val]
                output[index]=curr
            if curr in nums1:
                stack.append(curr)
        return output

print(nextGreaterElement(arr1,arr2))