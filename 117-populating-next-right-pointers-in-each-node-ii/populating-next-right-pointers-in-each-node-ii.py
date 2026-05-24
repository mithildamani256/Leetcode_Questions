# """
# # Definition for a Node.
# class Node(object):
#     def __init__(self, val=0, left=None, right=None, next=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next
# """

# class Solution(object):
#     def connect(self, root):
#         """
#         :type root: Node
#         :rtype: Node
#         """

#         if not root:
#             return None
        
#         if root.left:
#             if root.right:
#                 root.left.next = root.right
#             else:
#                 next_node = root.next

#                 while next_node:
#                     if next_node.left:
#                         root.left.next = next_node.left
#                         break

#                     if next_node.right:
#                         root.left.next = next_node.right
#                         break

#                     next_node = next_node.next
        
#         if root.right:
#             next_node = root.next

#             while next_node:
#                 if next_node.left:
#                     root.right.next = next_node.left
#                     break

#                 if next_node.right:
#                     root.right.next = next_node.right
#                     break

#                 next_node = next_node.next
        
#         self.connect(root.right)
#         self.connect(root.left)

#         return root
        
# #           1
# #          / \
# #         2-> 3
# #        / \   \
# #       4   7    6
# #      / \   \
# #     7-> 8.  9

# # start at root. then i know that for the root.left , the next pointer would be to root.right
# # for root.right, the next pointer would be the next pointer to root, and then root.left if root.left else root.right.
# # for root.left, if there is no root.right, then we access the root.next = next and then next.left if next.left otherwise next.right. 

# # start at 1 -> if root.left: root.left.next = root.left.next = root.right or root.next.left or root.next.right
# # look at 2 -> if root.left: root.left.next = root.right or root.next.left or root.next.right
# # look at 5 -> if root.right: root.right.next = root.next.left or root.next.right if root.next else None


# #     cur   1
# #          / \
# #     nxt 2-> 3
# #        / \   \
# #       4   7    6
# #      / \   \
# #     7-> 8.  9

# #

class Solution(object):

    def connect(self, root):

        cur = root

        while cur:

            dummy = Node(0)
            tail = dummy

            while cur:

                if cur.left:
                    tail.next = cur.left
                    tail = tail.next

                if cur.right:
                    tail.next = cur.right
                    tail = tail.next

                cur = cur.next

            cur = dummy.next

        return root
