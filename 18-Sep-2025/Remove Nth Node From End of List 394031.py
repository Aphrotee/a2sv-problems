# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        position = 0
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        position = length - n + 1
        dummy = ListNode(-1, head)
        prev = dummy
        curr = head
        steps = 0
        while curr:
            steps += 1
            if steps == position:
                prev.next = curr.next
                return dummy.next
            prev = curr
            curr = curr.next
