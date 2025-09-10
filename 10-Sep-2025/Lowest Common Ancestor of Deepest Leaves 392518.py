# Problem: Lowest Common Ancestor of Deepest Leaves - https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(root, 0)])
        depth = 0
        while queue:
            node, d = queue.popleft()
            depth = max(depth, d)

            if node.left is not None:
                queue.append((node.left, d + 1))
            if node.right is not None:
                queue.append((node.right, d + 1))
            
        self.potentialRoot = defaultdict(bool)
        def dfs(node, d):
            nonlocal depth
            if node is None:
                return False
            if d == depth:
                can_be_root = True
            else:
                left = dfs(node.left, d + 1)
                right = dfs(node.right, d + 1)
                can_be_root = left or right
            self.potentialRoot[node.val] = can_be_root
            return can_be_root
        
        dfs(root, 0)
        self.lca = None
        self.getLCA(root)
        return self.lca

    def getLCA(self, node):
        if node is None:
            return False
        if (node.left is not None and self.potentialRoot[node.left.val]) and \
            (node.right is not None and self.potentialRoot[node.right.val]):
            self.lca = node
        elif node.left is None and node.right is None:
            self.lca = node
        elif node.left is not None and self.potentialRoot[node.left.val]:
            self.getLCA(node.left)
        elif node.right is not None and self.potentialRoot[node.right.val]:
            self.getLCA(node.right)