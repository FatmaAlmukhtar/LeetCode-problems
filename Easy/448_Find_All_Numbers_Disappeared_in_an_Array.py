class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)

        return res


if __name__ == "__main__":
    assert Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5,6]
    assert Solution().findDisappearedNumbers([1,1]) == [2]
