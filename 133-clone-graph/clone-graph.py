"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return None

        hashmap = {}

        def dfs(node):
            if node in hashmap:
                return hashmap[node]

            new_node = Node(node.val)
            hashmap[node] = new_node

            for neighbour in node.neighbors:
                new_neighbour = dfs(neighbour)
                new_node.neighbors.append(new_neighbour)

            return new_node
        
        return dfs(node)
        


        