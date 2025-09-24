class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict = {arr2[i] : i for i in range(len(arr2))}
        arr1.sort(key=lambda x: (dict.get(x, len(arr2)), x))
        return arr1