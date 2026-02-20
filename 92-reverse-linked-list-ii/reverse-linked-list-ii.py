# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

        if not head or not head.next or left == right:
            return head

        dummy = ListNode()
        dummy.next = head

        before = dummy

        for _ in range(left - 1):
            before = before.next
        
        cur = before.next
        prev = None

        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        node = before.next
        before.next = prev
        node.next = nxt

        return dummy.next
        

        


        
        