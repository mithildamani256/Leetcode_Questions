# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # if not head:
        #     return head

        # cur = head
        # p = 0

        # while cur:
        #     p += 1
        #     cur = cur.next

        # k = k % p

        # if k == 0:
        #     return head

        # v = p - k

        # slow = head
        # fast = head

        # for _ in range(v):
        #     fast = fast.next
        
        # while fast:
        #     slow = slow.next
        #     fast = fast.next
        
        # new_head = slow.next
        # slow.next = None

        # dummy = new_head

        # while dummy:
        #     if dummy.next is not None:
        #         dummy = dummy.next
        #     else:
        #         break
        
        # dummy.next = head

        # return new_head

        if not head or not head.next or k == 0:  # ✅ Handle edge cases
            return head

        # Step 1: Compute length
        cur = head
        p = 1
        while cur.next:
            cur = cur.next
            p += 1
        tail = cur  # ✅ Store tail for later reconnection

        # Step 2: Optimize k
        k = k % p  # ✅ Ensure no extra rotations
        if k == 0:
            return head  # ✅ No change needed

        # Step 3: Find new head (Stop before breaking)
        v = p - k
        slow = head
        for _ in range(v - 1):  # ✅ Stop one before breaking
            slow = slow.next

        # Step 4: Rotate list
        new_head = slow.next
        slow.next = None  # ✅ Break the list
        tail.next = head  # ✅ Connect end to old head

        return new_head  # ✅ Return new hea

        