class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                   '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        res = []

        def backtracking(i, s):
            if len(s) == len(digits):
                res.append(s)
                return

            for c in mapping[digits[i]]:
                backtracking(i+1, s+c)


        if digits:
            backtracking(0, '')

        return res

if __name__ == "__main__":
    assert Solution().letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
