# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if not head:
            return None

        length = 1

        cur = head

        while cur.next:
            cur = cur.next
            length += 1

        joining_node = cur

        k = k % length

        if k == 0:
            return head

        fast = head

        for _ in range(k):
            fast = fast.next

        slow = head

        while fast.next:
            slow = slow.next
            fast = fast.next

        end_node = slow
        new_head = end_node.next
        joining_node.next = head
        end_node.next = None

        return new_head


#   head     end. new. joining_point
# 1 -> 2 -> 3 -> 4 -> 5
#  k = 2

#  4 -> 5 ->       1 -> 2 -> 3

# k > len(List) => k = k % len(list)
# keep a pointer for the last node in the list = 5
#  slow, fast pointers to get to (len(list) - k)th node = 3
#  next node = (len(list) - k)th node. next = 4
#  3.next = None
# last node.next = 1
# return 4