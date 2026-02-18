# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        current = dummy

        while list1 or list2:
            if list1 and list2:
                if list1.val > list2.val:
                    current.next = ListNode(list2.val)
                    list2 = list2.next
                else:
                    current.next = ListNode(list1.val)
                    list1 = list1.next
                current = current.next

            elif list1:
                current.next = ListNode(list1.val)
                current = current.next

                list1 = list1.next
            
            else:
                current.next = ListNode(list2.val)
                current = current.next

                list2 = list2.next  

        return dummy.next
                
        