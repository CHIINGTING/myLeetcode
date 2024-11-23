class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)  # 將字典轉換為集合，加速查找
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # 空字串可以被成功分割

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # 只要找到一個有效分割就可以停止內層迴圈

        return dp[n]