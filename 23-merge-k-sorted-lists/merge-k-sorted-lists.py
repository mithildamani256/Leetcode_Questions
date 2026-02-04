import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        
        # push the head of each list into heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val,node))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val,node.next))

        return dummy.next
