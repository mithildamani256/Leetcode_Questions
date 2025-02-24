# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        current = head
        lst = []

        while current:
            lst.append(current.val)
            current = current.next

        lst = sorted(lst)

        update = head
        i = 0

        while update:
            update.val = lst[i]
            update = update.next
            i += 1

        return head