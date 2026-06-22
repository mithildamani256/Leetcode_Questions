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

        dummy = ListNode()
        dummy.next = head

        fast = dummy
    
        for _ in range(n):
            fast = fast.next

        slow = dummy

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next

#  1 -> 2 -> 3 -> 4 -> 5

# n = 5
# 