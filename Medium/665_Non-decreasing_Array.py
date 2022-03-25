class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 2:
            return True

        counter = 0

        for i in range(0,len(nums)-1):
            if nums[i] > nums[i+1]:
                counter += 1

                if i>0 and nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]

        return counter <= 1
