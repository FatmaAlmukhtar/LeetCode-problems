class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        s = str(n)
        mySet = set()

        while n!=1:

            sum = 0

            if n in mySet:
                return False
            mySet.add(n)

            for i in s:
                sum += int(i)**2

            s = str(sum)
            n = sum

        return True


if __name__ == "__main__":
    assert Solution().isHappy(19) == True
    assert Solution().isHappy(1) == True
    assert Solution().isHappy(2) == False
