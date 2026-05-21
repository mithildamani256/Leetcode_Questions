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

        if not head:
            return None
        
        dummyLower = ListNode()
        lower = dummyLower

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
        
        lower.next = dummyGreater.next
        greater.next = None

        return dummyLower.next

    
# 1 -> 4 -> 3 -> 5, value is 4

# 1 -> 3 -> 4 -> 5 

# lower: 1 -> 3
# greater: 4 -> 5

# 1 -> 3 -> 4 -> 5