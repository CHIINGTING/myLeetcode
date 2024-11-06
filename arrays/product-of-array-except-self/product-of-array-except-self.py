class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer = [1] * length

        # 計算每個元素的左側乘積
        left_product = 1
        for i in range(length):
            answer[i] = left_product
            left_product *= nums[i]

        # 計算每個元素的右側乘積，並同時計算最終結果
        right_product = 1
        for i in range(length - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer