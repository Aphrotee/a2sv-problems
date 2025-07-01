# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]

        while queue:
            node = queue.pop(0)

            if node.left is not None:
                if node.left.val != node.val:
                    return False
                queue.append(node.left)
            if node.right is not None:
                if node.right.val != node.val:
                    return False
                queue.append(node.right)
        return True