# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True

        def dfs(node):
            if node is None:
                return 0
            
            if self.ans == False:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            if abs(left - right) > 1:
                self.ans = False

            return 1 + max(left, right)
        
        dfs(root)
        return self.ans