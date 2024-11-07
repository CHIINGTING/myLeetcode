class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # 判斷最小值在右側還是左側
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
