# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int

        """

        def helper(root, current_sum):

            if not root:
                return 0
            
            current_sum = current_sum * 10 + root.val
            
            if not root.left and not root.right:
                return current_sum

            return helper(root.left, current_sum) + helper(root.right, current_sum)

        return helper(root, 0)
            
