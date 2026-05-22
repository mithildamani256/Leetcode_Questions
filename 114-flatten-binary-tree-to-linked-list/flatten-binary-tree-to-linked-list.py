# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """

        if not root:
            return None

        left_tree = root.left
        right_tree = root.right

        root.left = None

        left_tail = self.flatten(left_tree)
        right_tail = self.flatten(right_tree)

        if left_tail:
            root.right = left_tree
            left_tail.right = right_tree 
        else:
            root.right = right_tree

        return right_tail or left_tail or root

#           1
#          / \
#         2.  5

# 1 -> 2 -> 5

# if not root: return None
# left_tree = root.left  n
# right_tree = root.right n
# root.left = None
# left_tail = helper(left_tree) n
# if left_tail:
    # root.right = left_tree n
    # if left_tail : left_tail.right = right_tree 
# else:
    # right_tail = helper(right_tree)
    # root.right = right_tree
# return right_tail or left_tail or root

# 1 -> 2 -> 5