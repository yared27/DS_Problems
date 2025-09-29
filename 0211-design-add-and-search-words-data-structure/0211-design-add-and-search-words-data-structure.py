class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            index = ord(w) - ord("a")
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True
        
    def search(self, word: str) -> bool:
        return self.search_helper(word, 0, self.root)
    
    def search_helper(self, word, pos, node):
        if pos == len(word):
            return node.is_end
        
        c = word[pos]
      
        if c == ".":
                for ch in node.children:
                    if ch != None and self.search_helper(word, pos+1, ch):
                        return True 
                return False
        else:
            index = ord(c) - ord("a")
            if node.children[index] is None:
                return False
            
            return self.search_helper(word, pos+1, node.children[index])

        
        

            

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)