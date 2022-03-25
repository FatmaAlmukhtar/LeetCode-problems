class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        def reverse(word, left, right):
            while left<right:
                word[left], word[right] = word[right], word[left]
                left = left+1
                right = right-1

            return ''.join(word)

        lst = s.split(' ')

        for i in range(len(lst)):
            lst[i] = reverse(list(lst[i]), 0, len(lst[i])-1)

        return ' '.join(lst)

if __name__ == "__main__":
    assert Solution().reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
