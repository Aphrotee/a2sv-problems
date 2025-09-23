# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def dfs(node):
            nonlocal ans
            if node is None:
                return False
            isP = False
            isQ = False
            if node is p:
                isP  = True
            elif node is q:
                isQ = True
            checkLeft = dfs(node.left)
            checkRight = dfs(node.right)

            if checkLeft and checkRight:
                ans = node
            elif (isP or isQ) and (checkLeft or checkRight):
                ans = node
            return checkLeft or checkRight or isP or isQ
        dfs(root)
        return ans