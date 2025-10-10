# Problem: Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float("-inf")

        def dfs(node):
            nonlocal max_path_sum
            if node is None:
                return 0
            
            leftSum = max(0, dfs(node.left))
            rightSum = max(0, dfs(node.right))
            
            subTree = max(leftSum, rightSum)
            max_path_sum = max(max_path_sum, node.val + leftSum + rightSum, node.val + subTree, node.val)
            
            return max(node.val + subTree, node.val) 
        dfs(root)
        return max_path_sum