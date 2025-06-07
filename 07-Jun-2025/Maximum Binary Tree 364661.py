# Problem: Maximum Binary Tree - https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        maxIdx = 0
        n = len(nums)
        root = None
        if n > 0:
            for i in range(n):
                if nums[i] > nums[maxIdx]:
                    maxIdx = i

            root = TreeNode(nums[maxIdx])
            root.left = self.constructMaximumBinaryTree(nums[:maxIdx])
            root.right = self.constructMaximumBinaryTree(nums[maxIdx + 1:])
            # print(self.levelOrder(root))
        return root
        

    def createSubTree(self, arr: List[int]) -> Optional[TreeNode]:
        dummy = TreeNode(-1)

        def addNode(node, num):
            if num > node.val:
                if node.right is not None:
                    addNode(node.right, num)
                else:
                    node.right = TreeNode(num)
            elif num < node.val:
                if node.left is not None:
                    addNode(node.left, num)
                else:
                    node.left = TreeNode(num)
        print(arr)
        for num in arr:
            print(num)
            addNode(dummy, num)
        
        return dummy.right
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        out = []
        q.append(root)
        while q:
            store = []
            iterations = len(q)
            for i in range(iterations):
                node = q.popleft()
                if node:
                    store.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if store:
                out.append(store)
        return out