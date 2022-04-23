# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def dfs(l, r):
            if l and r:
                return l.val == r.val and dfs(l.left, r.right) and dfs(l.right, r.left)
            return l == r

        return dfs(root.left, root.right)
