# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])

        ans = []
        while queue:
            level = []
            levelSize = len(queue)

            for _ in range(levelSize):
                node = queue.popleft()
                if node is not None:
                    level.append(node.val)
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
            if level:
                ans.append(level)
        return ans