# Problem: Clone Graph - https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(root, prev):
            if root is None:
                return None
            if root in visited:
                return visited[root]
            newNode = Node(root.val)
            visited[root] = newNode
            for node in root.neighbors:
                newNode.neighbors.append(dfs(node, newNode))
            return newNode
        return dfs(node, None)