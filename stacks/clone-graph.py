"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        return self.clone(node, {})
    
        # it use hashmap to store visited clone

    # use hashmap to store visited
    def clone(self, node, hashmap):
        # if not existed return null
        if not node:
            return None
        # if visited put in hashmap
        if node.val in hashmap:
            return hashmap[node.val]
        
        cloned = Node(node.val, [])
        hashmap[node.val] = cloned

        for neighbor in node.neighbors:
            cloned.neighbors.append(self.clone(neighbor, hashmap))
        
        return cloned