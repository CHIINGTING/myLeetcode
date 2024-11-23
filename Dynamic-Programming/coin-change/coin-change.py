class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 初始化 dp 陣列，大小為 amount + 1
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 湊成金額 0 所需硬幣數為 0

    # 遍歷每一個硬幣
        for coin in coins:
            for i in range(coin, amount + 1):
            # 更新 dp[i]
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # 如果 dp[amount] 仍為無限大，返回 -1，否則返回 dp[amount]
        return dp[amount] if dp[amount] != float('inf') else -1
