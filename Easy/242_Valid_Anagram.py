class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        lst_t = list(t)

        for i in s:
            if i not in lst_t:
                return False
            else:
                lst_t.remove(i)

        return True

        # one line code
        #return sorted(s)==sorted(t)


if __name__ == "__main__":
    assert Solution().isAnagram('car','rat') == False
    assert Solution().isAnagram('anagram','nagaram') == True
    assert Solution().isAnagram('aacc','ccac') == False
