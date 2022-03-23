class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        for i in range(len(s)):
            if i+1<len(s) and roman_numerals[s[i]] < roman_numerals[s[i+1]]:
                res -= roman_numerals[s[i]]
            else:
                res += roman_numerals[s[i]]
        return res


if __name__ == "__main__":
    assert Solution().romanToInt('MCMXCIV') == 1994
