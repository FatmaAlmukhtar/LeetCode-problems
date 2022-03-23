class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        lst = []

        parentheses = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in parentheses:
                if len(lst)>0 and lst[-1] == parentheses[char]:
                    lst.pop()
                else:
                    return False
            else:
                lst.append(char)


        if len(lst) == 0:
            return True
        else:
            False



if __name__ == "__main__":
    assert Solution().isValid('([])') == True
