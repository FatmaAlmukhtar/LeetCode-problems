class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        # sliding window
        left = 0
        right = k-1

        res = float('inf')

        while right < len(nums):
            res = min(res, nums[right]-nums[left])
            left += 1
            right += 1

        return res
