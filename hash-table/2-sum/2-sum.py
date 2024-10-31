from itertools import combinations
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = combinations(range(len(nums)), 2)

        result = next(((i, j) for i, j in indices if nums[i] + nums[j] == target), None)
        return result
