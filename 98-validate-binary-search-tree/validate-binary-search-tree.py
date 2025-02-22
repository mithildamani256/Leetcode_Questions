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

        def dfs(root):
            if not root:
                return []

            return dfs(root.left) + [root.val] + dfs(root.right)

        lst1 = dfs(root)

        l = set(lst1)

        lst2 = sorted(lst1)

        if lst1==lst2 and len(l) == len(lst1):
            return True
        
        return False
        