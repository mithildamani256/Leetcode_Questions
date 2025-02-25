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

        length = 0

        current = head

        while current:
            current = current.next
            length += 1
        
        iterate = length - n

        dummy = ListNode()
        current = dummy
        dummy.next = head

        for _ in range(iterate):
            current = current.next

        current.next = current.next.next

        return dummy.next