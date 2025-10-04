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
        prev = None
        fast, slow = head, head
        while fast is not None:
            prev = slow
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        prev.next = None
        listA = head
        listB = self.reverse(slow)

        curr = listA
        while listB is not None:
            nextA = listA.next
            nextB = listB.next if listB is not None else None
            curr.next = listB
            curr = curr.next
            curr.next = nextA
            curr = curr.next
            listA = nextA
            listB = nextB
        return head
    
    def reverse(self, head):
        dummy = ListNode()
        curr = head
        while curr is not None:
            nextNode = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = nextNode
        return dummy.next

        
        