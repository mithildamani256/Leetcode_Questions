"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return None

        queue = deque([root])

        while queue:
            size = len(queue)
            prev = None  # Keeps track of the previous node in the same level
            
            for _ in range(size):
                node = queue.popleft()  # Remove from front of queue

                if prev:
                    prev.next = node  # Link previous node to current node
                
                prev = node  # Update previous node
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # The last node in the level should point to None (already default)

        return root  # Return the modified tree