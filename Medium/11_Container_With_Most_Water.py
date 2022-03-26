class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height)-1
        area = 0

        while left<right:
            if min(height[left],height[right])*(right-left) > area:
                area = min(height[left],height[right])*(right-left)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area


if __name__ == "__main__":
    assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49
