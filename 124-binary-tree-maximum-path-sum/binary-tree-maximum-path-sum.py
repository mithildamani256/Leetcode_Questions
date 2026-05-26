# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.res = float('-inf')

        def include(root):
            if not root:
                return 0

            left_max = include(root.left)
            right_max = include(root.right)

            max_result = root.val + max(left_max, right_max, left_max + right_max)
            max_result = max(max_result, root.val)

            max_return = root.val + max(left_max, right_max)
            max_return = max(max_return, root.val)

            self.res = max(self.res, max_result)

            return max_return

        include(root)

        return self.res


#           -10
#           /. \
#          9.   20 
#              /. \
#             15   7

# if i include -10
# and then i try to find the max path in left and right:
# from left, i include 9 and then left and right just give 0
# from right, i include 20 + max(left, right). -
# from left, i get 15 and from right i get 7.   |
#  returns 20 + 15                            <-

# max global. now whatever i return for this i update max. so res bacomes = max(res, 35)


#       2
#      /  \
#    -1.   -2