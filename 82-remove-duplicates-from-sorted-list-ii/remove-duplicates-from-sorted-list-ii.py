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

        dummy = ListNode()
        dummy.next = head

        new = dummy
        cur = head

        while cur:
            prev = None
            while cur.next and cur.val == cur.next.val:
                if not prev:
                    prev = cur
                cur = cur.next
            
            if (prev and prev != cur):
                cur = cur.next
                continue
            
            new.next = cur
            new = new.next
            cur = cur.next
        
        new.next = None

        return dummy.next


        



# dummy = dummyNode()
# dummy.next = head
# new = dummy
# prev = None
# cur = head

# while cur:
#   prev = None
    # while cur.next and cur.val == cur.next.val:
    #     if not prev:
    #           prev = cur
    #     cur = cur.next

    # if (prev and prev != cur):
    #       cur = cur.next
    #       continue

    #new.next = cur
    #new = new.next
    # cur = cur.next
# new.next = None


#prev        new                                        cur
#           1         ->          2           ->          2 

# new=> 1 -> None