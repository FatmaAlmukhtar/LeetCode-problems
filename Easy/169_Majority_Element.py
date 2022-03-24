class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mySet = set()
        myDictionary = {}
        for i in sorted(nums):
            if i not in mySet:
                count = 0
                mySet.add(i)
                myDictionary[i] = count
            else:
                count+=1
                myDictionary[i] = count

        return max(myDictionary, key = myDictionary.get)

if __name__ == "__main__":
    assert Solution().majorityElement([2,2,1,1,1,2,2]) == 2
