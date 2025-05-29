# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        queue = [(root, 0)]
        if root is None:
            return False
        while queue:
            node, cur_sum = queue.pop(0)
            

            cur_sum += node.val
            if node.left is None and node.right is None:
                if cur_sum == targetSum:
                    return True
            else:
                if node.left is not None:
                    queue.append((node.left, cur_sum))
                if node.right is not None:
                    queue.append((node.right, cur_sum))
        return False