# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def dfs(node, depth):
            nonlocal max_depth
            if node is None:
                max_depth = max(depth, max_depth)
                return
            depth += 1
            dfs(node.left, depth)
            dfs(node.right, depth)
        dfs(root, 0)
        return max_depth
