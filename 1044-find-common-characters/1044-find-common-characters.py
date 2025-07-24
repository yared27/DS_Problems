class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
        for word in words[1:]:
            common &= Counter(word)
        res = []
        for char, freq in common.items():
            res.extend([char] * freq)
        return res
