# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        numberOfNodes = 1
        curr = head
        newHead = head
        while curr is not None:
            if numberOfNodes == k:
                newHead = curr
            numberOfNodes += 1
            curr = curr.next
        numberOfNodes -= 1
        self.reverse(ListNode(-1), head, k, numberOfNodes // k)
        return newHead
        
    
    def reverse(self, prev, head, k, groups):
        if groups == 0:
            return
        curr = head
        count = 0
        nextPrev = head
        while curr is not None and count < k:
            
            nextNode = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = nextNode
            count += 1
        head.next = curr
        
        self.reverse(nextPrev, curr, k, groups - 1)
            
