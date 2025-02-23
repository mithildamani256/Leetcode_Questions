# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def helper(root, left, right):
            if not root:
                return True
            
            if root.val <= left or root.val >= right:
                return False
            
            return helper(root.left, left, root.val) and helper(root.right, root.val, right)

        return helper(root, float('-inf'), float('inf'))