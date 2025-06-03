# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return [] 
        
        stack = [root]
        answer = []
        visited = set()

        while stack:
            node = stack[-1]
            while node.left is not None and node.left not in visited:
                stack.append(node.left)
                visited.add(node.left)
                node = node.left
            node = stack.pop()
            answer.append(node.val)
            if node.right is not None and node.right not in visited:
                stack.append(node.right)
                visited.add(node.right)
        return answer