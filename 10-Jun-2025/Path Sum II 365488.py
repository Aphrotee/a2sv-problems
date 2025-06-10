# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []

        def search(node, path, pathSum):
            if node is None:
                return
            path.append(node.val)
            pathSum += node.val
            if node.left is None and node.right is None:
                if pathSum == targetSum:
                    answer.append(path[:])
            else:
                search(node.left, path, pathSum)
                search(node.right, path, pathSum)
            path.pop()
        
        search(root, [], 0)
        return answer