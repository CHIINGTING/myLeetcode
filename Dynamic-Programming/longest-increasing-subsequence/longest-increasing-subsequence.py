class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n == 0:
            return 0

        # 初始化 dp 陣列，每個元素初始值為 1
        dp = [1] * n

        # 填充 dp 陣列
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # 返回 dp 陣列中的最大值
        return max(dp)
