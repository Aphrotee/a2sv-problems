# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.answer = None
        self.foundP = False
        self.foundQ = False

        def dfs(node):
            if node is None:
                return False
            node_is_target = False
            if node == p:
                node_is_target = True
                self.foundP = True
            if node == q:
                self.foundQ = True
                node_is_target = True
            left_search = False
            right_search = False
            if ((not self.foundP) and p.val < node.val) or ((not self.foundQ) and q.val < node.val):
                left_search = dfs(node.left)
            if ((not self.foundP) and p.val > node.val) or ((not self.foundQ) and q.val > node.val):
                right_search = dfs(node.right)

            if left_search or right_search:
                if (left_search and right_search) or node_is_target:
                    self.answer = node
                return True
            
            return node_is_target
        dfs(root)
        return self.answer