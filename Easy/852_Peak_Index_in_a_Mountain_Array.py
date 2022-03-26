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


#### using binary search
"""
class Solution(object):
    def peakIndexInMountainArray(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = (lo + hi) / 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
"""
if __name__ == "__main__":
    assert Solution().peakIndexInMountainArray([0,10,5,2]) == 1
