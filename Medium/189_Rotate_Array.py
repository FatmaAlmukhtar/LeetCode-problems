class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left = left+1
                right = right-1


        # reverse entire array in-place
        reverse(0, len(nums)-1)
        # reverse the left portion of the array upto k elements
        reverse(0, k-1)
        # reverse the right portion from the k element to the end of the array
        reverse(k, len(nums)-1)
