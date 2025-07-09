from collections import deque

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Step 1: BFS to build parent mapping and find startNode
        queue = deque([root])
        parent = {}
        startNode = None

        while queue:
            node = queue.popleft()
            if node.val == startValue:
                startNode = node
            if node.left:
                parent[node.left.val] = node
                queue.append(node.left)
            if node.right:
                parent[node.right.val] = node
                queue.append(node.right)

        def backtrack_path(node, path_tracker):
            path = []
            while node in path_tracker:
                node, direction = path_tracker[node]
                path.append(direction)
            return ''.join(reversed(path))

        queue = deque([startNode])
        visited_nodes = set([startNode])
        path_tracker = {}

        while queue:
            node = queue.popleft()
            if node.val == destValue:
                return backtrack_path(node, path_tracker)

            if node.val in parent:
                p = parent[node.val]
                if p not in visited_nodes:
                    path_tracker[p] = (node, 'U')
                    queue.append(p)
                    visited_nodes.add(p)

            if node.left and node.left not in visited_nodes:
                path_tracker[node.left] = (node, 'L')
                queue.append(node.left)
                visited_nodes.add(node.left)

            if node.right and node.right not in visited_nodes:
                path_tracker[node.right] = (node, 'R')
                queue.append(node.right)
                visited_nodes.add(node.right)

        return ""
