class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # 找到目標值
            if nums[mid] == target:
                return mid

            # 判斷左半區間是否有序
            if nums[left] <= nums[mid]:
                # 目標值在左半區間內
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:  # 否則在右半區間
                    left = mid + 1
            else:
                # 右半區間有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:  # 否則在左半區間
                    right = mid - 1
        return -1

