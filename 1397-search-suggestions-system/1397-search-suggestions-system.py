class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.suggestion = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for w in word:
            index = ord(w) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
            
            if len(curr.suggestion) < 3:
                curr.suggestion.append(word)

    def getSuggestion(self, prefix):
        curr = self.root
        res = []
        for w in prefix:
            index = ord(w) - ord('a')
            if curr:
                curr = curr.children[index]
                res.append(curr.suggestion if curr else [])
            else:
                res.append([])
        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products.sort()

        for product in products:
            trie.insert(product)
        
        return trie.getSuggestion(searchWord)


