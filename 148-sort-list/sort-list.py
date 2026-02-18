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

        def merge(left, right):
            dummy = ListNode()
            cur = dummy

            while left or right:
                if left and right:
                    if left.val > right.val:
                        cur.next = right
                        right = right.next
                    else:
                        cur.next = left
                        left = left.next
                
                elif left:
                    cur.next = left
                    left = left.next
                
                else:
                    cur.next = right
                    right = right.next

                cur = cur.next
            
            return dummy.next

        def search(node):
            if not node or not node.next:
                return node 

            length = 0
            cur = node

            while cur:
                cur = cur.next
                length += 1
            
            mid = length // 2
            dummy = ListNode()
            dummy.next = node
            cur = dummy

            for _ in range(mid):
                cur = cur.next
            
            right = cur.next
            cur.next = None

            left_sorted = search(node)
            right_sorted = search(right)

            return merge(left_sorted, right_sorted)
        
        return search(head)

