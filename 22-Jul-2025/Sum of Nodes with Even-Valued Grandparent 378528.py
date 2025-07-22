# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        evens = []
        queue = [root]
        while queue:
            node = queue.pop(0)

            if node.val % 2 == 0:
                evens.append((node, 0))
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        answer = 0
        while evens:
            node, dist = evens.pop(0)
            if dist == 2:
                answer += node.val
                continue
            if node.left is not None:
                evens.append((node.left, dist + 1))
            if node.right is not None:
                evens.append((node.right, dist + 1))
        return answer

