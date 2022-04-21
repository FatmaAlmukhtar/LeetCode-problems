class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)

        for i,num in enumerate(nums):
            dp[i] = max(dp[i-1] + num, num)

        return max(dp)
