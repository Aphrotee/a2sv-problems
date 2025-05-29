# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        queue = [(root, float("-inf"), float("inf"))]
        while queue:

            node, lowerBound, upperBound = queue.pop(0)

            if not (lowerBound < node.val < upperBound):
                # check if the current node's value is not in bounds, defeating the definiton of a binary search tree
                return False
        
            # traverse the left child node and make the current value of the node the upper bound
            if node.left is not None:
                queue.append((node.left, lowerBound, node.val))

            # traverse the right child node and make the current value of the node the lower bound
            if node.right is not None:
                queue.append((node.right, node.val, upperBound))

        return True

        # def checkValidity(node: Optional[TreeNode], lower: int, upper: int) -> bool:
        #     if node is None:
        #         return True
            
        #     if not (lower < node.val < upper):
        #         return False
        #     return checkValidity(node.left, lower, node.val) and\
        #            checkValidity(node.right, node.val, upper)
        
        # return checkValidity(root, float("-inf"), float("inf"))
            