# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(node):
            nonlocal ans
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                ans = False
            return 1 + max(left, right)
        dfs(root)
        return ans