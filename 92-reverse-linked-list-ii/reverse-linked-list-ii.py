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

        current = head
        length = 0

        while current:
            current = current.next
            length += 1
        
        if length == 0 or length == 1 or left == right:
            return head

        dummy = ListNode(-501)
        new_head = dummy
        dummy.next = head

        for _ in range(left - 1):
            new_head = new_head.next

        dummy = ListNode()
        new_tail = dummy
        dummy.next = head

        for _ in range(right + 1):
            new_tail = new_tail.next

        dummy = ListNode()
        leftNode = dummy
        dummy.next = head

        for _ in range(left):
            leftNode = leftNode.next

        dummy = ListNode()
        rightNode = dummy
        dummy.next = head

        for _ in range(right):
            rightNode = rightNode.next  

        prev = None
        lefty = leftNode

        for _ in range(right - left + 1):
            nxt = lefty.next
            lefty.next = prev
            prev = lefty
            lefty = nxt

        leftNode.next = new_tail

        if left != 1:
            new_head.next = prev
            return head
        else:
            return prev
        
        
