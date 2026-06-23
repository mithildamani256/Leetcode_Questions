# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        heap = []

        for node in lists:
            if node:
                heap.append((node.val,node))

        heapq.heapify(heap)
        
        dummy = ListNode()
        cur = dummy
        
        while heap:
            _, node = heapq.heappop(heap)
            
            cur.next = node
            cur = cur.next

            node = node.next

            if node:
                heapq.heappush(heap, (node.val, node))

        return dummy.next
        