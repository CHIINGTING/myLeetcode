class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        return sorted(self.result(nums))

    def result(self, nums):
        left = 0
        right = (len(nums) - 1)
        while left <= right:
            if abs(left) < abs(right):
                yield nums[right] ** 2
                right -= 1
            else:
                yield nums[left] ** 2
                left += 1
