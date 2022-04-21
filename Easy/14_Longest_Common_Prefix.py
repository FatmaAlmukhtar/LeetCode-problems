class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""

        for i in range(len(min(strs))):
            c = strs[0][i]

            if all(st[i] == c for st in strs):
                res += c
            else:
                break

        return res
