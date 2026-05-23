# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def helper(root, current_value):
            if not root:
                return 0

            new_value = current_value * 10 + root.val

            if not root.left and not root.right:
                return new_value
            
            return helper(root.left, new_value) + helper(root.right, new_value)

        if not root:
            return 0

        return helper(root, 0)


#           4
#          / \
#         5.  7
#        / \.  \
       #1. 2.   3

# current_value = 4

# helper(root.left, 4) + helper(root.right,4)

# if not root:
#       return 0
# new_value = current_value * 10 + root.val
# if not root.left and not root.right:
#           return new_value

# helper(root.left, new_value) + helper(root.right, new_value)
