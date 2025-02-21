# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        
        if not root:
            return 0

        q = deque([root])
        lst = []

        while q:
            size = len(q)
            avg = 0

            for _ in range(size):
                node = q.popleft()

                avg += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            lst.append(avg / float(size))

        return lst



