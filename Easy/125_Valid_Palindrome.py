class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s)-1

        while l < r:
            a = s[l].lower()
            b = s[r].lower()

            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    l += 1
                    r -= 1

            l = l + (not a.isalnum())
            r = r - (not b.isalnum())

        return True
