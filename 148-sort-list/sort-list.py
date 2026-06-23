class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        # split list into two halves
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        left = head

        # sort both halves
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)

        # merge sorted halves
        return self.merge(left_sorted, right_sorted)

    def merge(self, left, right):
        dummy = ListNode()
        cur = dummy

        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next

            cur = cur.next

        cur.next = left if left else right
        return dummy.next