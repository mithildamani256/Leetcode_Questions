# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        stack = []
        counter = 0
        cur = root 

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            current_element = stack.pop()
            counter += 1

            if counter == k:
                return current_element.val

            cur = current_element.right
        
        return

#            3
#          /. \ 
#         1.   4
#          \
#           2 , k = 3

# stack = [3]

# pop 3.  counter = 3 
# return 3


# iterative inorder dfs traversal
# stack = []
# cur = root
# coutner = 0
# while cur:
#       stack.append(cur)
#       cur = cur.left

# element = stack.pop()
# counter += 1

#  if counter == k:
#       return element

# cur = element.right

# while cur:
#       stack.append(cur)
#       cur = cur.left

