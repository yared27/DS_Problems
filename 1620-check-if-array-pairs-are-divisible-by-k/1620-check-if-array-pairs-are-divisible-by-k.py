class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:  
        counter = Counter()
        noPaired = 0

        for i in range(len(arr)):
            rem = arr[i] % k
            if counter[rem]:   
                noPaired += 1
                counter[rem] -= 1
            else:
                counter[(-rem) % k] += 1  

        return noPaired == len(arr) // 2


