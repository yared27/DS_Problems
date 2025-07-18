class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0
        for x, freq in count.items():
            group_size = x + 1
            groups = (freq + group_size - 1) // group_size  
            total += groups * group_size
        return total
