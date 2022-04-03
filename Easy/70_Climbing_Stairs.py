class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        dp[0] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
