# Problem: Reorder List - https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None or head.next.next is None:
            return head
        self.length = 0
        self.count = 0
        self.front = head
        self.nextNode = head.next
        def traverse(node):
            if node is None:
                return
            self.length += 1
            traverse(node.next)
            if self.count < (self.length // 2):
                self.front.next = node
                node.next = self.nextNode
                self.front = self.nextNode
                if self.nextNode is not None:
                    self.nextNode = self.nextNode.next
            elif self.count == (self.length // 2) + 1:
                self.front.next = None
            self.count += 1

        traverse(head)
        return head

