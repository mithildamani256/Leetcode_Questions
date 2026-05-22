# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if not head:
            return None

        length = 0

        cur = head

        while cur:
            cur = cur.next
            length += 1
        
        if length == 1:
            return head

        middle = 0

        if length % 2 == 0:
            middle = length // 2
        else:
            middle = (length // 2) + 1

        prev = head

        for _ in range(middle - 1):
            prev = prev.next

        cur = prev.next
        start = cur
        next_cur = cur.next

        while next_cur:
            later = next_cur.next
            next_cur.next = cur

            cur = next_cur
            next_cur = later

        prev.next = cur
        start.next = None

        dummy = ListNode()
        dummy.next = head
        result = dummy

        start = head
        end = cur

        for _ in range(middle):
            if start:
                result.next = start
                start = start.next

                result = result.next

            if end:
                result.next = end
                end = end.next

                result = result.next

        result.next = None

        return dummy.next


                                                          # prev                   cur  
#       1       ->          2       ->      3       ->      4           ->          5

# result => 1 -> 5 -> 2 -> 4 -> 3

# length = 6
# middle = 3

# length = 5
# middle = (5 // 2 ) + 1

       
# 1 -> 2 -> 3 -> 4 = middle = 2 

# start.      end
#  1 -> 2 - > 4 -> 3


# 1 -> 2-> 3 -> 4 -> 5 = middle = 3
# 1 -> 2 -> 3 -> 5 -> 4 