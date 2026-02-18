# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        def dfs(root, target):
            if not root:
                return False
            
            if not root.left and not root.right:
                if root.val == target:
                    return True
                return False
            
            new_target = target - root.val

            return dfs(root.left, new_target) or dfs(root.right, new_target)

        
        return dfs(root, targetSum)
        