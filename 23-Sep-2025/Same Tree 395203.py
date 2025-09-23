# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def serialize(node):
            if node is None:
                return "#"
        
            serialization = f"{node.val}L{serialize(node.left)}R{serialize(node.right)}"
            return serialization
        
        return serialize(p) == serialize(q)
