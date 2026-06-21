# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.res = 0

        def dfs(root):
            if not root:
                return -1

            left_d = dfs(root.left)
            right_d = dfs(root.right)

            self.res = max(self.res, left_d + right_d + 2)

            return 1 + max(left_d, right_d)

        dfs(root)

        return self.res

        
        

#       1
#      /  \
#     2.   3
#    /. \
#   4.   5
#       / \
#      6.  7
# at each step, you would update the global varialble as 
# global variable = max(global variable, 2 + root.left + root.right)

# return 1 + max(root.left, root.right)