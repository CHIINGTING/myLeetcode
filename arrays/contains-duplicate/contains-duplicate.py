class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        items={}
        for i in iter(nums):
            if i not in items:
                items[i] = 1
            else:
                return True
        return False