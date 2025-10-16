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
        visited = set()
        ans = []
        while stack:
            # print(ans, stack)
            topNode = stack[-1]
            if topNode.left is not None and topNode.left not in visited:
                stack.append(topNode.left)
                visited.add(topNode.left)
                continue

            node = stack.pop()
            ans.append(node.val)
            if node.right is not None and node.right not in visited:
                stack.append(node.right)
                visited.add(node.right)
        return ans


            
        