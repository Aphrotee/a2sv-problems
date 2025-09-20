# Problem: Flatten a Multilevel Doubly Linked List - https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/?envType=problem-list-v2&envId=linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node()
        dummy.next = head
        def mergeChild(node, prev):
            curr = node
            while curr is not None:
                if curr.child is not None:
                    nextNode = curr.next
                    curr.next = curr.child
                    lastNode = mergeChild(curr.child, prev)
                    curr.child.prev = curr
                    if nextNode:
                        nextNode.prev = lastNode
                    lastNode.next = nextNode
                    curr.child = None
                    prev = lastNode
                    curr = lastNode.next
                else:
                    prev = curr
                    curr = curr.next
            return prev
        mergeChild(head, dummy)
        return dummy.next