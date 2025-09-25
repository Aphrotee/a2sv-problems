# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def checkNode(node, lower, upper):
            nonlocal ans
            if node is None:
                return
            if not (lower < node.val < upper):
                ans = False
            
            checkNode(node.left, lower, node.val)
            checkNode(node.right, node.val, upper)
        checkNode(root, float("-inf"), float("inf"))
        return ans
        