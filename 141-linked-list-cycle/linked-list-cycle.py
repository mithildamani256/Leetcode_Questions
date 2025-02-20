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

        visited = set()
        
        while head:
            if head in visited:
                return True

            visited.add(head)

            head = head.next

        return False

            
