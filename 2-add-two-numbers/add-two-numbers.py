# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        carry = 0
        dummy = ListNode(0)
        res = dummy
        
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            total = a + b + carry
            res.next = ListNode(total % 10)

            res = res.next

            carry = total // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if carry:
                res.next = ListNode(carry)
            
        return dummy.next

