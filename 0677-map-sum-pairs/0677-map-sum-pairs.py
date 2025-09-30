class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.is_end = False
        self.value = None
class MapSum:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, key: str, val: int) -> None:
        curr = self.root

        for w in key:
            index = ord(w) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.value = val
        curr.is_end = True
        

    def sum(self, prefix: str) -> int:
        curr = self.root 

        for w in prefix:
            index = ord(w) - ord('a')
            if curr.children[index] is None:
                return 0
            curr = curr.children[index]
        return self.dfs(curr)
    
    def dfs(self, node:TrieNode):
        if node is None:
            return 0
        
        total = node.value if node.is_end else 0

        for child in node.children:
            total += self.dfs(child)
        
        return total
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)