# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        curr1, curr2 = l1, l2
        dummy = ListNode()
        curr = dummy
        while carry > 0 or curr1 is not None or curr2 is not None:

            n1 = curr1.val if curr1 is not None else 0
            n2 = curr2.val if curr2 is not None else 0
            total = carry + n1 + n2
            rem = total % 10
            carry = total // 10
            newNode = ListNode(rem)
            curr.next = newNode
            curr = curr.next
            if curr1 is not None:
                curr1 = curr1.next
            if curr2 is not None:
                curr2 = curr2.next
        return dummy.next