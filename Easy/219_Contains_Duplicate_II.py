class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        visited = {}

        for i in range(len(nums)):
            if nums[i] in visited and i - visited[nums[i]] <= k:
                return True
            visited[nums[i]] = i

        return False
        
