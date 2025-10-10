# Problem: Construct Binary Tree from Preorder and Inorder Traversal - https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        inorderMap = {value: index for index, value in enumerate(inorder)}
        preIdx = 0

        def insertNode(left, right):
            nonlocal preIdx
            inIdx = inorderMap[preorder[preIdx]]
            node = TreeNode(preorder[preIdx])
            if left < inIdx:
                preIdx += 1
                node.left = insertNode(left, inIdx - 1)
            if right > inIdx:
                preIdx += 1
                node.right = insertNode(inIdx + 1, right)
            return node
        return insertNode(0, n - 1)
        
        