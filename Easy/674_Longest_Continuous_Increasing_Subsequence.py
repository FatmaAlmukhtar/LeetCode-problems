class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c1 = 0
        c2 = 0
        for i in range(len(nums)):
            if i!=len(nums)-1 and nums[i] < nums[i+1]:
                c1 += 1

            else:
                c1 += 1
                c2 = max(c1, c2)
                c1 = 0

            if i==len(nums)-1:
                c1 += 1
                c2 = max(c1, c2)
        return c2
