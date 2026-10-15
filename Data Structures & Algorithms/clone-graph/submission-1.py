"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone={}

        def dfs(cur):
            if cur in clone:
                return clone[cur]
            copy=Node(cur.val)
            clone[cur]=copy

            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy
        return dfs(node)
