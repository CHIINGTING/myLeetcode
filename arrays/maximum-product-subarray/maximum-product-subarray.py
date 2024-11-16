class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.findtMax(nums)

    def findtMax(self,nums):
        current_min = nums[0]
        current_max = nums[0]
        max_product = nums[0]
        for item in range(1,len(nums)):
            num = nums[item]

            # 如果遇到負數，交換 current_max 和 current_min
            if num < 0:
                current_max, current_min = current_min, current_max

            # 更新當前最大和最小值
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)

            # 更新全局最大值
            max_product = max(max_product, current_max)
        return max_product
