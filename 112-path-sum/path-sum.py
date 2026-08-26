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
                return root.val == target
            
            return dfs(root.left, target - root.val) or dfs(root.right, target - root.val)

        return dfs(root, targetSum)