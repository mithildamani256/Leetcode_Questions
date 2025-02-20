# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # def dfs(root):
        #     if not root:
        #         return ""

        #     value = str(root.val)
        #     result = [value]

        #     for s in dfs(root.left):
        #         result.append(value + s)

        #     for s in dfs(root.right):
        #         result.append(value + s)

        #     return result

        # result1 = dfs(root.left)
        # result2 = dfs(root.right)
        # sum = 0

        # for val in result1:
        #     sum += int(str(root.val) + val)
        # for val in result2:
        #     sum += int(str(root.val) + val)

        # return sum

        def dfs(node, current_sum):
            if not node:
                return 0  # Base case: No node, return 0

            current_sum = current_sum * 10 + node.val  # Accumulate number

            # If it's a leaf node, return the formed number
            if not node.left and not node.right:
                return current_sum

            # Recurse for left and right subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)


            
