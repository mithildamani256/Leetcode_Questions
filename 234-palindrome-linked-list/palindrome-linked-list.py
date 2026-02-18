# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
        cur = head 
        lst = []

        while cur:
            lst.append(cur.val)
            cur = cur.next
        
        for i in range(len(lst) // 2):
            if lst[i] != lst[len(lst) - 1 - i]:
                return False
        return True