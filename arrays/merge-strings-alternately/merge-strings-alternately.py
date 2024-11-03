class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1 = ''.join(self.generator(word1, word2))
        return word1

    def generator(self, word1, word2):
        i, j = 0, 0
        # 交替從 word1 和 word2 中取字元
        while i < len(word1) and j < len(word2):
            yield word1[i]
            yield word2[j]
            i += 1
            j += 1
        # 如果 word1 有剩餘字元
        while i < len(word1):
            yield word1[i]
            i += 1
        # 如果 word2 有剩餘字元
        while j < len(word2):
            yield word2[j]
            j += 1
