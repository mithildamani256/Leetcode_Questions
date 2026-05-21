# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        for _ in range(length // k):
            start = prev.next
            next_left = start.next

            left_node = start

            for _ in range(k - 1):
                later = next_left.next
                next_left.next = left_node
                left_node = next_left
                next_left = later

            prev.next = left_node
            start.next = next_left
            prev = start

        return dummy.next
                 

# 1 -> 2 -> 3 -> 4
# k = 2


# prev = dummynode
# start = 1
# left_node = 1
# next_left = 2

# after that one for loop iteration:
# prev = dummynode
# start = 1
# left_node = 2
# next_left = 3

# dummynode -> 1 <- 2 -> 3 -> 4

# prev.next = leftnode
# start.next = next_left

# dummy -> 2 -> 1 -> 3 -> 4

# prev = start (1)
# start = prev.next
# left_node = start
#  next_left = start.next