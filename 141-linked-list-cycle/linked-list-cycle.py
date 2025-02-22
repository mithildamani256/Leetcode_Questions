# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        visit = []

        while head:
            if head in visit:
                return True
            visit.append(head)
            head = head.next

        return False
            
