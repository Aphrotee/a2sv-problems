# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        adj = {}
        queue = deque([root])
        source = None
        dest = None
        while queue:
            node = queue.popleft()
            if node.val == startValue:
                source = node
            elif node.val == destValue:
                dest = node
            if node not in adj:
                adj[node] = []
            if node.left is not None:
                adj[node].append((node.left, "L"))
                if node.left not in adj:
                    adj[node.left] = []
                adj[node.left].append((node, "U"))
                queue.append(node.left)
            if node.right is not None:
                adj[node].append((node.right, "R"))
                if node.right not in adj:
                    adj[node.right] = []
                adj[node.right].append((node, "U"))
                queue.append(node.right)
        self.path = []
        self.answer = []
        visited = set()
        def dfs(node):
            nonlocal adj
            nonlocal visited
            if node.val == destValue:
                self.answer = self.path[:]
                return True
            if node in visited:
                return False
            visited.add(node)

            
            for neighbour, direction in adj[node]:
                self.path.append(direction)
                if neighbour not in visited:
                    
                    if dfs(neighbour):
                        return True
                self.path.pop()
            return False
        dfs(source)
        return ''.join(self.answer)