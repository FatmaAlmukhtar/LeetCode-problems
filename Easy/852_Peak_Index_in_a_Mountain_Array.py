class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        if len(arr) < 3:
            return None


        for i in range(len(arr)):
            if i!=0 and i!=len(arr)-1 and arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                return i

        return None


if __name__ == "__main__":
    assert Solution().peakIndexInMountainArray([0,10,5,2]) == 1
