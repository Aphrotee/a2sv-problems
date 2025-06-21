# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = 0
        queue = [(root, 0)]

        while queue:
            node, num = queue.pop(0)

            num = (num * 10) + node.val

            if node.left is None and node.right is None:
                answer += num
            else:
                if node.left is not None:
                    queue.append((node.left, num))
                if node.right is not None:
                    queue.append((node.right, num))
        return answer