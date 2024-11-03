class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        aws = 0

        for num in iter(nums):
            if num is not val:
                nums[aws] = num
                aws += 1
        nums[aws:] = '_' * (len(nums) - aws)
        return aws
