class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.is_end = False
        self.freq = 0

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for w in word:
            index = ord(w) - ord("a")
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True
        curr.freq += 1

    def countWordFreq(self, words):
        curr = self.root
        for w in words:
            index = ord(w) - ord('a')
            if curr.children[index] is None:
                return 0
            curr = curr.children[index]
        return curr.freq if curr.is_end else 0

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        trie = Trie()

        for word in words:
            trie.insert(word)
        ans = []
        
        freq_map = {word : trie.countWordFreq(word)  for word in words}
        sorted_words = sorted(freq_map.keys(), key=lambda x: (-freq_map[x], x))
        return sorted_words[:k]

