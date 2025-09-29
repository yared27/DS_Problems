class TrieNode():
    def __init__(self):
        self.children = [None, None]
class Trie():
    def __init__(self):
        self.root = TrieNode()
    def insert(self, num):
        curr = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if curr.children[bit] is None:
                curr.children[bit] = TrieNode() 
            curr = curr.children[bit]
    def findMaximumXOR(self, num):
        curr = self.root
        xor_sum = 0
        for i in range(31, -1, -1):
            bit = (num >> i)&1
            opposite_bit = 1 - bit 
            if curr.children[opposite_bit]:
                xor_sum |= (1 << i)
                curr = curr.children[opposite_bit]
            else:
                curr = curr.children[bit]
        return xor_sum
           
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        trie = Trie()

        for num in nums:
            trie.insert(num)
        
        max_xor = 0

        for num in nums:
            max_xor = max(max_xor, trie.findMaximumXOR(num))
        return max_xor