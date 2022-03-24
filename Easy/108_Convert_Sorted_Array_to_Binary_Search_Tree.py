# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def recursion(nums):

            if len(nums)==0 or nums==None:
                return None

            if len(nums)==1:
                return TreeNode(nums[0])

            mid = len(nums) // 2
            root = TreeNode(nums[mid])

            root.left = recursion(nums[0:mid])
            root.right = recursion(nums[mid+1: len(nums)])

            return root


        return recursion(nums)
