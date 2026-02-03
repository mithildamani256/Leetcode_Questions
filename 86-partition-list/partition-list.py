# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

        dummyLesser = ListNode()
        lower = dummyLesser

        dummyGreater = ListNode()
        greater = dummyGreater

        cur = head

        while cur:
            if cur.val < x:
                lower.next = cur
                lower = lower.next
            else:
                greater.next = cur
                greater = greater.next

            cur = cur.next

        greater.next = None
        lower.next = dummyGreater.next

        return dummyLesser.next
        