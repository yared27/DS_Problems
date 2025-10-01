class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0
    
class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.is_end = True
        curr.count += 1
   
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        noSubSeq = 0
        for word in words:
            trie.insert(word)
        q = deque()
        q.append((0, trie.root))
        
        while q:
            index , node = q.popleft()
            if node.is_end:
                noSubSeq += node.count
                node.is_end =  False
            for ch, child in node.children.items():
                pos = s.find(ch, index)
                if pos != -1:
                    q.append((pos + 1, child))

        return noSubSeq