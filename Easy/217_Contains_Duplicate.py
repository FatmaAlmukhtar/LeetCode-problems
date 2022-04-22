class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # using sorting time O(nlogn) space O(1)
        nums = sorted(nums)

        for i in range(len(nums)):
            if i<len(nums)-1 and nums[i]==nums[i+1]:
                return True

        return False

        # using hash table time O(n) space O(n)
        visited = set()

        for i in nums:
            if i in visited:
                return True
            visited.add(i)

        return False
