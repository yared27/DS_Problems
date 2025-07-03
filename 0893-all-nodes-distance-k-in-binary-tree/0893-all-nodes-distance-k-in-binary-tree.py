# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        q = collections.deque([root])
        dic = {}
        visited ={}
        while q: 
            node = q.popleft()
            if node.left:
                q.append(node.left)
                dic[node.left.val]=node
            if node.right:
                q.append(node.right)
                dic[node.right.val]=node

        q.append(target)
        while k>0 and q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                visited[node.val]=1
                if node.left and node.left.val not in visited:
                    q.append(node.left)
                if node.right and node.right.val not in visited:
                    q.append(node.right)
                if node.val in dic and dic[node.val].val not in visited:
                    q.append(dic[node.val])
            k-=1
        while q:
            ans.append(q.popleft().val)
        return ans




