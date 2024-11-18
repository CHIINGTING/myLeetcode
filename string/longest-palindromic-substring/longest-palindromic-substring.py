class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s
        longest = ""
        for i in range(len(s)):
            # 奇數回文
            odd_palindrome = self.expandAroundCenter(s, i, i)
            # 偶數回文
            even_palindrome = self.expandAroundCenter(s, i, i + 1)

            # 更新最長回文子字串
            longest = max(longest, odd_palindrome, even_palindrome, key=len)

        return longest
    def expandAroundCenter(self, s, left, right):
        # 從中心擴展，直到不符合回文條件
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 返回回文子字串
        return s[left + 1:right]
