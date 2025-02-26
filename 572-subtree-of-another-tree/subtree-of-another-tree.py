# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def sameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
        