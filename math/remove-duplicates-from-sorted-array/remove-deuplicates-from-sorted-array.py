class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 建立一個生成器，依次產生唯一元素
        def unique_elements(nums):
            previous = None
            for num in nums:
                if num != previous:
                    yield num
                    previous = num

        # 使用生成器來填充唯一的元素到 nums 前部分
        k = 0
        for unique in unique_elements(nums):
            nums[k] = unique
            k += 1

        # 將 k 之後的元素設為佔位符 "_"
        nums[k:] = ['_'] * (len(nums) - k)

        return k
