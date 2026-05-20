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

        dummy = ListNode(0)
        result = dummy

        while list1 or list2:
            if list1 and list2:
                if list1.val >= list2.val:
                    result.next = ListNode(list2.val)
                    list2 = list2.next
                else:
                    result.next = ListNode(list1.val)
                    list1 = list1.next
            elif list1:
                result.next = ListNode(list1.val)
                list1 = list1.next
            else:
                result.next = ListNode(list2.val)
                list2 = list2.next

            result = result.next

        return dummy.next


#  while list1 or list2:
    # if list1 and list2:
    #       compare list1.val and list2.val:
            # and based on that: add value to result and increment for correct list
    # if list1:
        # result.next = ListNode(list1.val)
        # list1 = list1.next
        # result = result.next
        