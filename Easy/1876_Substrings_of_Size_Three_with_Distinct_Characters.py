class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 2
        count = 0

        while right < len(s):
            if len(set(s[left:right+1])) == 3:
                   count += 1

            left += 1
            right += 1

        return count
