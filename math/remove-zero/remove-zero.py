class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        aws=0
        for num in iter(nums):
            if num is not 0:
                nums[aws] = num
                aws += 1
        for i in range(len(nums)-aws):
            nums[i+aws] = 0
            i += 1

        return aws