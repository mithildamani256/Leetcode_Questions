# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        if head is None:
            return head
        
        current = head
        length = 0

        while current:
            length += 1
            current = current.next
        
        if length == 1:
            return None
        
        p = length - n

        dummy = ListNode()
        dummy.next = head
        slow = dummy

        for _ in range(p):
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next