class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # 更新最低買入價
            if price < min_price:
                min_price = price
            # 計算當前利潤，並更新最大利潤
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
