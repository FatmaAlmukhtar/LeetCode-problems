class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        for plot in range(len(flowerbed)):
            if plot!=0 and plot!=len(flowerbed)-1 and flowerbed[plot]==0:
                if flowerbed[plot+1]==0 and flowerbed[plot-1]==0:
                    n -= 1
                    flowerbed[plot] = 1

            elif plot==0 and flowerbed[plot]==0:
                if plot!=len(flowerbed)-1 and flowerbed[plot+1]==0:
                    n -= 1
                    flowerbed[plot] = 1
                elif plot == len(flowerbed)-1:
                    n -= 1
                    flowerbed[plot] = 1

            elif plot == len(flowerbed)-1 and flowerbed[plot]==0:
                if flowerbed[plot-1]==0:
                    n -= 1
                    flowerbed[plot] = 1

        return n <= 0
