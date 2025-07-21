# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = {}
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node not in adj:
                adj[node] = []
            if node.left is not None:
                adj[node].append(node.left)
                if node.left not in adj:
                    adj[node.left] = []
                adj[node.left].append(node)
                queue.append(node.left)
            if node.right is not None:
                adj[node].append(node.right)
                if node.right not in adj:
                    adj[node.right] = []
                adj[node.right].append(node)
                queue.append(node.right)

        queue = [(target, 0)]
        visited = set()
        answer = []
        while queue:
            node, dist = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)
            if dist == k:
                answer.append(node.val)
            for neighbour in adj[node]:
                if neighbour not in visited:
                    queue.append((neighbour, dist + 1))
        return answer