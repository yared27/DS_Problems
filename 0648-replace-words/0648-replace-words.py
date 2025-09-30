class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.is_end = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for w in word:
            index = ord(w) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True
    
    def getBase(self, word):
        prefix = ''
        curr = self.root 
        for w in word:
            index = ord(w) - ord('a')
            if curr.children[index] is None:
                return word
            curr = curr.children[index]
            prefix += w
            if curr.is_end:
                return prefix
        return word
            
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for dic in dictionary:
            trie.insert(dic)
        ans = []
        for word in sentence.split():
            ans.append(trie.getBase(word))
        
        return " ".join(ans)