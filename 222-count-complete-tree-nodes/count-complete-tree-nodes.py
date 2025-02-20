# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        # Compute leftmost height
        leftHeight = 0
        leftNode = root
        while leftNode:
            leftHeight += 1
            leftNode = leftNode.left
        
        # Compute rightmost height
        rightHeight = 0
        rightNode = root
        while rightNode:
            rightHeight += 1
            rightNode = rightNode.right
        
        # If left height equals right height, it's a perfect tree
        if leftHeight == rightHeight:
            return (2 ** leftHeight) - 1
        
        # Otherwise, recurse for left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)      

