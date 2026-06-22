# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        cur = head
        dummy = ListNode()
        node = dummy
        
        while cur:
            flag = False

            while cur.next and cur.next.val == cur.val:
                cur = cur.next
                flag = True
            
            if flag:
                cur = cur.next
                continue
            else:
                node.next = cur
                node = node.next
                cur = cur.next
        
        node.next = None
        return dummy.next



# 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5

# cur = 1
# while cur.next and cur.next.val == cur.val:
#           flag = True
#           cur = cur..next
# if flag :
#       cur = cur.next
#       continue
# else:
#       node.next = cur
#       node = node.next
#       cur = cur.next
        