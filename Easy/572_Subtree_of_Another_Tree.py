# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        if subRoot==None:
            return True
        if root==None:
            return False

        if self.isSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSame(self, root, subRoot):
        if root==None and subRoot==None:
            return True

        if root and subRoot and root.val == subRoot.val:
            return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)

        return False
