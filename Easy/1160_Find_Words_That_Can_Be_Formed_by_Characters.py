class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        counter = 0
        sum = 0
        for word in words:
            for c in word:
                if chars.count(c) >= word.count(c):
                    counter += 1
                else:
                    break

            if counter == len(word):
                sum += len(word)

            counter = 0

        return sum
