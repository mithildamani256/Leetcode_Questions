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

        if not head:
            return None

        if left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy

        for _ in range(left - 1):
            cur = cur.next
        
        left_before = cur
        start = left_before.next

        left_node = start
        next_left = start.next

        for _ in range(right - left):
            later = next_left.next

            next_left.next = left_node
            left_node = next_left
            next_left = later

        left_before.next = left_node
        start.next = next_left

        return dummy.next

#  1 -> 2 -> 3 -> 4 -> 5
#  2 <- 3 <- 4 
#  left = 2, next_l = 3 , next_left = 4
#  next_l.next = left, left = next_l, next_l = next_left
# 