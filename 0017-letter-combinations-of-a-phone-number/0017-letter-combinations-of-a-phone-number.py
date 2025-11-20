class Solution:
    def solve(self, digits, mapping, ans, output, index):
        if(index >= len(digits)):
            ans.append(output)
            return
        
        number = int(digits[index])
        value = mapping[number]

        for ch in value:
           
            self.solve(digits, mapping, ans, output+ch, index+1)

    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="": return []
        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
  
        self.solve(digits, mapping, ans, "", 0)
        return ans