class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """


        lst = s.split(' ')

        while '' in lst:
            lst.remove('')
        left = 0
        right = len(lst)-1

        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

        return ' '.join(lst)
