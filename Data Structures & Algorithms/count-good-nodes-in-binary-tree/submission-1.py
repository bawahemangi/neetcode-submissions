# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxval):
            count=0
            if not node:
                return 0
            if node.val>=maxval:
                maxval=node.val
                count=1
            count+=dfs(node.left,maxval)
            count+=dfs(node.right,maxval)
            return count
        return dfs(root,root.val)