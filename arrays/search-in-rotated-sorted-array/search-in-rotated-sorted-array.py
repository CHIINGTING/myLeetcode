class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # 如果找到目標值
            if nums[mid] == target:
                return mid
            # 判斷左半部分是否有序
        if nums[left] <= nums[mid]:
            # 如果 target 在左半部分範圍內
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # 否則右半部分有序
        else:
            # 如果 target 在右半部分範圍內
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

