class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root 
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.is_end = True 
    def checkWords(self, prefix):
        curr = self.root
        for w in prefix:
            if w not in curr.children or not curr.children[w].is_end:
                return False
            curr = curr.children[w]
        return True
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = Trie()

        for word in words:
            trie.insert(word)
        words.sort()
        word = ""
        for prefix in words:
           if trie.checkWords(prefix):
                if len(prefix) > len(word):
                    word = prefix
       
        return word
            
            

