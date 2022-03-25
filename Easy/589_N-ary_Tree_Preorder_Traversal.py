"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stack = []

        def recursion(root):

            if root:
                stack.append(root.val)
                for node in root.children:
                    recursion(node)

        recursion(root)

        return stack
